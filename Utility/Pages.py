from PageFragments.LoginPage import LoginPage
from PageFragments.MainPage import MainPage


class Pages:

    driver = None

    def main_page(self):
        main_page = MainPage()
        main_page.driver = self.driver
        return main_page

    def login_page(self):
        login_page = LoginPage()
        login_page.driver = self.driver
        return login_page
