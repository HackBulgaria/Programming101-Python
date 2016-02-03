import sqlite3
from client import Client
from validation import get_validator, StrongPasswordException
from helpers import hash_password
import messages


conn = sqlite3.connect("bank.db")
conn.row_factory = sqlite3.Row
cursor = conn.cursor()


def create_clients_table():
    create_query = '''create table if not exists
        clients(id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT,
                password TEXT,
                salt TEXT,
                balance REAL DEFAULT 0,
                message TEXT)'''

    cursor.execute(create_query)


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


def login(username, password):
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
