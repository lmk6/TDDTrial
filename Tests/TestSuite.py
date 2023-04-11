import sys
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from project import LoggingApp, WebApp, Exceptions


class TestWebpage(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get('http://127.0.0.1:5000/')

    def tearDown(self):
        self.driver.quit()

    def test_main_page_title_is_correct(self):
        self.assertIn('Home Page', self.driver.title)

    def test_main_page_navbar_with_Login_btn(self):
        login_btn = self.driver.find_element(By.ID, "LogInBtn")
        self.assertIsNotNone(login_btn)
        self.assertIn("LogIn", login_btn.text)

    def test_log_in_window_appears_with_email_and_password_boxes_in_login_container(self):
        self.assertIsNotNone(self.driver.find_element(By.ID, "logInContainer"))

        email_box_id, pass_box_id = "emailBox", "passwordBox"
        email_box = self.driver.find_element(By.ID, pass_box_id)
        password_box = self.driver.find_element(By.ID, pass_box_id)

        self.assertFalse(email_box.is_displayed())
        self.assertFalse(password_box.is_displayed())

        self.driver.find_element(By.ID, "LogInBtn").click()

        self.assertTrue(email_box.is_displayed())
        self.assertTrue(password_box.is_displayed())


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


def get_default_credentials():
    return "some@email.com", "some_password"
