import sys
import unittest
import os

sys.path.append("..")

import sql_manager


STRONG_PASSWORD1 = "123Asdf$$123Asdf"
STRONG_PASSWORD2 = "321$$321Asdf"


class SqlManagerTests(unittest.TestCase):

    def setUp(self):
        sql_manager.create_database()
        sql_manager.register('Tester', STRONG_PASSWORD1)

    def tearDown(self):
        sql_manager.cursor.execute('DROP TABLE clients')

    @classmethod
    def tearDownClass(cls):
        os.remove("bank.db")

    def test_register(self):
        sql_manager.register('Dinko', STRONG_PASSWORD2)

        sql_manager.cursor.execute('SELECT Count(*)  FROM clients WHERE username = (?)', ('Dinko',))
        users_count = sql_manager.cursor.fetchone()

        self.assertEqual(users_count[0], 1)

    def test_login(self):
        logged_user = sql_manager.login('Tester', STRONG_PASSWORD1)
        self.assertEqual(logged_user.get_username(), 'Tester')

    def test_login_sql_injection_in_the_username(self):
        logged_user = sql_manager.login("' OR 1=1 --", 'whatever')
        self.assertFalse(logged_user)

    def test_login_sql_injection_in_the_password(self):
        logged_user = sql_manager.login('Tester', "' OR 1=1 --")
        self.assertFalse(logged_user)

    def test_login_wrong_password(self):
        logged_user = sql_manager.login('Tester', STRONG_PASSWORD2)
        self.assertFalse(logged_user)

    def test_change_message(self):
        logged_user = sql_manager.login('Tester', STRONG_PASSWORD1)
        new_message = "podaivinototam"
        sql_manager.change_message(new_message, logged_user)
        self.assertEqual(logged_user.get_message(), new_message)

    def test_change_password(self):
        logged_user = sql_manager.login('Tester', STRONG_PASSWORD1)
        new_password = "12345"
        sql_manager.change_pass(new_password, logged_user)

        logged_user_new_password = sql_manager.login('Tester', new_password)
        self.assertEqual(logged_user_new_password.get_username(), 'Tester')

    def test_change_password_with_sql_injection(self):
        sql_manager.register('Dinko', STRONG_PASSWORD1)
        sql_manager.register('Vladko', STRONG_PASSWORD2)

        logged_user = sql_manager.login('Dinko', STRONG_PASSWORD1)
        new_password = "1234Asdf$$$Asdf' WHERE id = 3 --"
        sql_manager.change_pass(new_password, logged_user)
        self.assertFalse(sql_manager.login('Vladko', "1234Asdf$$$Asdf"))


if __name__ == '__main__':
    unittest.main()

