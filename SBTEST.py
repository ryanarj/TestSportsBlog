from Driver import Driver
import unittest
from PageFragments.MainPage import MainPage


class SBTEST(unittest.TestCase):

    def get_driver(self):
        path = 'http://127.0.0.1:8000/'
        return Driver(path).driver()

    def navigate_to_page(self, driver, page):
        driver.find_element_by_css_selector(MainPage().link_to_page(page)).click()

if __name__ == "__main__":
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(SBTEST)
    unittest.TextTestRunner().run(suite)
