import unittest
from Utility import Driver
from Strings.MainPageStrings import MainPageStrings as mainStrings
from Utility.Actions import Actions
from Utility.Pages import Pages
from Utility.Strings import Strings


class SBTEST(unittest.TestCase):

    driver = None
    actions = Actions()
    pages = Pages()
    strings = Strings()

    def setUp(self):
        Driver.initialize()

    def tearDown(self):
        Driver.close_driver()

    def GoToURL(self, url):
        self.driver = Driver.Instance
        self.actions.driver = self.driver
        self.pages.driver = self.driver
        Driver.Instance.get(url)

    def navigate_to(self, page):
        self.GoToURL(url=mainStrings.url_f.format(page))


if __name__ == "__main__":
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(SBTEST)
    unittest.TextTestRunner().run(suite)
