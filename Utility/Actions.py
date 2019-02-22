from Actions.LoginPageAction import LoginPageAction


class Actions:

    driver = None

    def login(self):
        login_action = LoginPageAction()
        login_action.driver = self.driver
        return login_action
