from Strings.MainPageStrings import MainPageStrings as mainStrings
from Utility.SBTEST import SBTEST


class TestSportsUser(SBTEST):

    def test_login_page(self):
        username = 'TestUser'
        password = 'Run@1234'

        # Navigate to the page and then login, once in, the page will be loaded
        self.navigate_to(mainStrings.login)
        self.actions.login().run(username=username, password=password, submit_btn=True)
        self.pages.main_page().wait_for_load()
