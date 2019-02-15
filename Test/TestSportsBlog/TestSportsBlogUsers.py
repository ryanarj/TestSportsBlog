from Actions.LoginPageAction import LoginPageAction
from SBTEST import SBTEST
from Strings.MainPageStrings import MainPageStrings


class TestSportsUser(SBTEST):

    def test_login_pages(self):
        wd = self.get_driver()
        username = 'admin'
        password = 'Test@1234'
        self.navigate_to_page(page=MainPageStrings().login, driver=wd)
        LoginPageAction().run(username=username, password=password, driver=wd)
        LoginPageAction().run(submit_btn=True, driver=wd)

