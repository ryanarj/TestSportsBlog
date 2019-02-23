from time import sleep

from PageFragments.LoginPage import LoginPage


class LoginPageAction:

    driver = None

    def wait_page_loaded(self):
        sleep(1)
        assert self.driver.find_element_by_css_selector(LoginPage().username_text()), \
            'Username does not text does not exist '
        assert self.driver.find_element_by_css_selector(LoginPage().password_text()),\
            'Password does not text does not exist '
        assert self.driver.find_element_by_css_selector(LoginPage().submit_btn()),\
            'Submit btn does not text does not exist '

    def run(self, username=None, password=None, submit_btn=None):
        self.wait_page_loaded()
        if username is not None:
            self.driver.find_element_by_css_selector(LoginPage().username_text()).send_keys(username)

        if password is not None:
            self.driver.find_element_by_css_selector(LoginPage().password_text()).send_keys(password)

        if submit_btn is not None:
            self.driver.find_element_by_css_selector(LoginPage().submit_btn()).submit()
