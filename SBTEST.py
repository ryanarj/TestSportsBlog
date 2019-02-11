from Driver import Driver
import unittest


class SBTEST(unittest.TestCase):

    def get_driver(self):
        return Driver(
            'https://stackoverflow.com/questions/39428042/use-selenium-with-chromedriver-on-mac').driver()

if __name__ == "__main__":
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(SBTEST)
    unittest.TextTestRunner().run(suite)
