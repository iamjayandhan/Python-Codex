class LoginStore:
    def __init__(self):
        self.data = {}

    def add_user(self, login, password):
        if login in self.data:
            raise AssertionError('User already exists')

        self.data[login] = password

    def check_user(self, login, password):
        if not login in self.data:
            return False

        if self.data[login] != password:
            return False

        return True


class LoginManager:
    def __init__(self):
        self.store = LoginStore()

    def _ask_input_and_password(self):
        username = input("username: ")
        password = input("password: ")
        return username, password

    def login_check(self):
        username, password  = self._ask_input_and_password()

        while not self.store.check_user(username, password):
            print("Wrong username or password")
            if input("Are you a new user?") == "y":
                print("Starting registration process")
                username, password = self._ask_input_and_password()
                self.store.add_user(username, password)
                print("Done. Try to login.")
            username, password  = self._ask_input_and_password()

manager = LoginManager()
manager.login_check()