import sqlite3
from client import Client
from validation import get_validator, StrongPasswordException
from helpers import hash_password
import messages

from settings import DB_NAME, SQL_STRUCTURE_FILE,\
                     BLOCK_AFTER_N_ATTEMPTS, BLOCKING_TIME
import os
import datetime
import time


def adapt_datetime(ts):
    return time.mktime(ts.timetuple())

sqlite3.register_adapter(datetime.datetime, adapt_datetime)


conn = sqlite3.connect(DB_NAME)
conn.row_factory = sqlite3.Row
cursor = conn.cursor()


class UserBlockedException(Exception):
    pass


def create_database():
    with open(SQL_STRUCTURE_FILE, 'r') as f:
        create_query = f.read()

    cursor.executescript(create_query)


# TODO: Better raise exception: UserNotFound
def get_id_by_username(username):
    query = """SELECT id FROM clients
               WHERE username = ?
               LIMIT 1"""
    cursor.execute(query, (username, ))
    result = cursor.fetchone()

    if result is None:
        return None

    return result['id']


def change_message(new_message, logged_user):
    update_sql = "UPDATE clients SET message = '%s' WHERE id = '%s'" % (new_message, logged_user.get_id())
    cursor.execute(update_sql)
    conn.commit()
    logged_user.set_message(new_message)


def change_pass(new_pass, logged_user):
    update_sql = """UPDATE clients
                    SET password = ?, salt = ?
                    WHERE id = ?"""
    pwd_hash, salt = hash_password(new_pass)

    cursor.execute(update_sql,
                   (pwd_hash, salt, logged_user.get_id()))
    conn.commit()


def register(username, password):
    validator = get_validator(username)

    if not validator.is_valid(password):
        raise StrongPasswordException(messages.STRONG_PASSWORD)

    hashed_password, salt = hash_password(password)
    insert_sql = """INSERT INTO clients (username, password, salt)
                    VALUES (?, ?, ?)"""

    cursor.execute(insert_sql, (username, hashed_password, salt))
    conn.commit()


def create_login_attempt(user_id, status):
    now = datetime.datetime.now()
    insert_sql = """INSERT INTO login_attempts(client_id,
                                               attempt_status,
                                               timestamp)
                    VALUES(?, ?, ?)"""

    cursor.execute(insert_sql, (user_id, status, now))
    conn.commit()


def block_if_necessary(user_id):
    query = """SELECT attempt_status
               FROM login_attempts
               WHERE client_id = ?
               ORDER BY id DESC
               LIMIT ?"""
    cursor.execute(query, (user_id, BLOCK_AFTER_N_ATTEMPTS))
    result = cursor.fetchall()

    if len(result) < BLOCK_AFTER_N_ATTEMPTS:
        return

    should_block = all([r['attempt_status'] == 'FAILED' for r in result])

    if not should_block:
        return

    create_login_attempt(user_id, status='BLOCKED')
    block_start = datetime.datetime.now()
    block_end = block_start + datetime.timedelta(seconds=BLOCKING_TIME)
    insert_sql = """INSERT INTO blocked_users(client_id,
                                              block_start,
                                              block_end)
                    VALUES(?, ?, ?)"""

    cursor.execute(insert_sql, (user_id, block_start, block_end))
    conn.commit()


def is_blocked(user_id):
    query = """SELECT block_end
               FROM blocked_users
               WHERE client_id = ?
               ORDER BY id DESC
               LIMIT 1"""
    cursor.execute(query, (user_id, ))

    r = cursor.fetchone()

    if r is None:
        return False

    now = datetime.datetime.now()
    return r['block_end'] > adapt_datetime(now)


def login(username, password):
    user_id = get_id_by_username(username)

    if is_blocked(user_id):
        raise UserBlockedException(messages.BLOCKED_MESSAGE)

    user = _login(username, password)

    if user:
        create_login_attempt(user.get_id(), status="SUCCESS")
        return user

    create_login_attempt(user_id, status="FAILED")
    block_if_necessary(user_id)

    return False


def _login(username, password):
    salt_query = """SELECT salt
                    FROM clients
                    WHERE username = ?
                    LIMIT 1"""
    cursor.execute(salt_query, (username,))
    auth_result = cursor.fetchone()

    if auth_result is None:
        return False

    pwd_hash, _ = hash_password(password, salt=auth_result['salt'])

    select_query = """SELECT id, username, balance, message
                      FROM clients
                      WHERE username = ? AND password = ?
                      LIMIT 1"""

    cursor.execute(select_query, (username, pwd_hash))
    user = cursor.fetchone()

    if(user):
        return Client(user[0], user[1], user[2], user[3])
    else:
        return False
