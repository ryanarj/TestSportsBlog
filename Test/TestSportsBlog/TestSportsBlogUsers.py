from Strings.MainPageStrings import MainPageStrings as mainStrings
from Utility.SBTEST import SBTEST


class TestSportsUser(SBTEST):

    def test_login_page(self):
        username = 'TestUser'
        password = 'Run@1234'

        self.navigate_to(mainStrings.login)
        self.actions.login().run(username=username, password=password)
