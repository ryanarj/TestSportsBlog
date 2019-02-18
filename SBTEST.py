
import unittest
import Driver


class SBTEST(unittest.TestCase):

    def setUp(self):
        Driver.initialize()

    def tearDown(self):
        Driver.close_driver()

    def GoToURL(self, url):
        Driver.Instance.get(url)
        return Driver.Instance

if __name__ == "__main__":
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(SBTEST)
    unittest.TextTestRunner().run(suite)
