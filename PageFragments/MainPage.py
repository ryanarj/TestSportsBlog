from time import sleep


class MainPage:

    driver = None

    def wait_for_load(self):
        sleep(1)
        assert self.driver.find_element_by_css_selector(self.page_header()), \
            'Not on main page'

    def page_header(self):
        return "article:nth-child(1)"

    def link_to_page(self, page_link):
        return "a[class='nav-item nav-link'][href='{}']".format(page_link)
