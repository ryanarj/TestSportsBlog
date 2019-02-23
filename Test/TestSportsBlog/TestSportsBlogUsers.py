from time import sleep
from Strings.MainPageStrings import MainPageStrings as mainStrings
from Utility.SBTEST import SBTEST


class TestSportsUser(SBTEST):

    def test_login_page(self):
        username = ['Test', 'TestUser']
        password = ['1234', 'Run@1234']

        # Navigate to the page and then login with wrong credentials
        self.navigate_to(mainStrings.login)
        self.actions.login().run(username=username[0], password=password[0], submit_btn=True)
        sleep(1)
        assert self.driver.find_element_by_css_selector(self.pages.login_page().inforbar_text()).text == \
            self.strings.error_strings().invalid_user

        # Clean the fields and login with correct user
        self.actions.login().run(clean_fields=True)
        self.actions.login().run(username=username[1], password=password[1], submit_btn=True)
        sleep(1)
        self.pages.main_page().wait_for_load()
