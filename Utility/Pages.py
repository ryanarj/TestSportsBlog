from PageFragments.MainPage import MainPage


class Pages:

    driver = None

    def main_page(self):
        main_page = MainPage()
        main_page.driver = self.driver
        return main_page
