from time import sleep
from PageFragments.LoginPage import LoginPage
from SBTEST import SBTEST


class LoginPageAction(SBTEST):

    def wait_page_loaded(self, driver, timeout=sleep(10)):
        assert driver.find_element_by_css_selector(LoginPage().username_text()), \
            'Username does not text does not exist '
        assert driver.find_element_by_css_selector(LoginPage().password_text()),\
            'Password does not text does not exist '
        assert driver.find_element_by_css_selector(LoginPage().submit_btn()),\
            'Submit btn does not text does not exist '

    def run(self, driver, username=None, password=None, submit_btn=None, result=None):
        self.wait_page_loaded(driver)
        if username is not None:
            driver.find_element_by_css_selector(LoginPage().username_text()).send_keys(username)

        if password is not None:
            driver.find_element_by_css_selector(LoginPage().password_text()).send_keys(password)

        if submit_btn is not None:
            driver.find_element_by_css_selector(LoginPage().submit_btn()).submit()
