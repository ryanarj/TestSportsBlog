
class LoginPage(object):

    def page_is_loaded(self):
        return ".content-section"

    def username_text(self):
        return ".textinput[name='username']"

    def password_text(self):
        return ".textinput[name='password']"

    def submit_btn(self):
        return ".btn[type='submit']"

