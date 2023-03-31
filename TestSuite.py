import unittest
import LoggingApp
import Exceptions

def get_default_credentials():
    return "some@email.com", "some_password"

class LoggingAppTest(unittest.TestCase):

    def test_logging_app_start(self):
        instance = LoggingApp.Application()
        self.assertIsNotNone(instance)

    def test_create_user_and_check_if_exists(self):
        instance = LoggingApp.Application()
        email, _ = get_default_credentials()
        instance.create_user(email, "password")
        self.assertTrue(instance.exists(email))

    def test_empty_email_and_password(self):
        instance = LoggingApp.Application()
        self.assertRaises(Exceptions.EmptyFieldException, lambda: instance.create_user('', ''))

    def test_create_duplicated_user(self):
        instance = LoggingApp.Application()
        email, password = get_default_credentials()
        instance.create_user(email, password)
        self.assertRaises(Exceptions.UserAlreadyExistsException, lambda: instance.create_user(email, password))

    def test_delete_user(self):
        instance = LoggingApp.Application()
        email, password = get_default_credentials()
        instance.create_user(email, password)
        instance.remove_user(email)
        self.assertTrue(not instance.exists(email))

        instance.create_user(email, password)
        instance.remove_user(email)
        self.assertRaises(Exceptions.UserDoesNotExistsException, lambda: instance.remove_user(email))

        instance.create_user(email, password)
        email2 = "some2@email"
        instance.create_user(email2, password)
        instance.remove_user(email)
        self.assertTrue(instance.exists(email2))


if __name__ == '__main__':
    unittest.main()
