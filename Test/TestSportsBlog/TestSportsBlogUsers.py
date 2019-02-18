from Actions.LoginPageAction import LoginPageAction
from SBTEST import SBTEST
from Strings.MainPageStrings import MainPageStrings as mainStrings


class TestSportsUser(SBTEST):

    def test_login_page(self):
        obj = self.GoToURL(url=mainStrings.url_f.format(mainStrings.login))
        username = 'TestUser'
        password = 'Run@1234'
        LoginPageAction().run(username=username, password=password, driver=obj)
        LoginPageAction().run(submit_btn=True, driver=obj)
        x = 1
