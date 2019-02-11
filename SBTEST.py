from Driver import Driver
import unittest


class SBTEST(unittest.TestCase):

    def get_driver(self):
        path = 'http://127.0.0.1:8000/'
        return Driver(path).driver()

if __name__ == "__main__":
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(SBTEST)
    unittest.TextTestRunner().run(suite)
