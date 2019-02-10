import Driver


class TestSportsBlog(Driver):

    def test_site_works(self):
        url_path = 'https://stackoverflow.com/questions/39428042/use-selenium-with-chromedriver-on-mac'
        wd = self.Driver(url=url_path)
        x = 1
