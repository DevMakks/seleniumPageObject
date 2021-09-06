from .base_page import BasePage
from .locators import BasePageLocators, LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "/login/" in self.browser.current_url, "URL after forwarding into Log in page doesn't contains '/login/'"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "should_be_login_form"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "should_be_register_form"

    def register_new_user(self, email, password):
        email_field = self.browser.find_element(*LoginPageLocators.EMAIL_FOR_REG)
        password_field = self.browser.find_element(*LoginPageLocators.PASSWORD_FOR_REG)
        conf_password_field = self.browser.find_element(*LoginPageLocators.CONFIRM_PASSWORD_FOR_REG)
        reg_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)

        email_field.send_keys(email)
        password_field.send_keys(password)
        conf_password_field.send_keys(password)
        reg_button.click()