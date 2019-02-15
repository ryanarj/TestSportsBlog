from Actions.LoginPageAction import LoginPageAction
from SBTEST import SBTEST


class TestSportsUser(SBTEST):

    def test_page_works(self):

        username = 'admin'
        password = 'Test@1234'

        LoginPageAction().run(username=username, password=password)
        LoginPageAction().run(submit_btn=True)
        x = 1

