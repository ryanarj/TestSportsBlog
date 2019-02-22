import unittest
from Actions.LoginPageAction import LoginPageAction
from Utility import Driver
from Strings.MainPageStrings import MainPageStrings as mainStrings
from Utility.Actions import Actions


class SBTEST(unittest.TestCase):

    driver = None
    actions = Actions()

    def setUp(self):
        Driver.initialize()

    def tearDown(self):
        Driver.close_driver()

    def GoToURL(self, url):
        global driver
        driver = Driver.Instance
        self.actions.driver = driver
        Driver.Instance.get(url)

    def navigate_to(self, page):
        self.GoToURL(url=mainStrings.url_f.format(page))


if __name__ == "__main__":
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(SBTEST)
    unittest.TextTestRunner().run(suite)
