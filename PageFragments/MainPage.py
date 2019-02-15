

class MainPage(object):

    def page_is_loaded(self):
        return "header"

    def link_to_page(self, page_link):
        return "a[class='nav-item nav-link'][href='{}']".format(page_link)
