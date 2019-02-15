from time import sleep
from PageFragments.LoginPage import LoginPage
from SBTEST import SBTEST


class LoginPageAction(SBTEST):

    def wait_page_loaded(self, timeout=sleep(10)):
        assert self.get_driver().find_element_by_css_selector(LoginPage().username_text()),\
            'Username does not text does not exist '
        assert self.get_driver().find_element_by_css_selector(LoginPage().password_text()),\
            'Password does not text does not exist '
        assert self.get_driver().find_element_by_css_selector(LoginPage().submit_btn()),\
            'Submit btn does not text does not exist '

    def run(self, username=None, password=None, submit_btn=None, result=None):

        if username is not None:
            self.get_driver().find_element_by_css_selector(LoginPage().username_text()).send_keys(username)
            assert self.get_driver().find_element_by_css_selector(LoginPage().username_text()).text == username

        if password is not None:
            self.get_driver().find_element_by_css_selector(LoginPage().password_text()).send_keys(password)
            assert self.get_driver().find_element_by_css_selector(LoginPage().password_text()).text == password

        if submit_btn is not None:
            self.get_driver().find_element_by_css_selector(LoginPage().submit_btn()).submit()
