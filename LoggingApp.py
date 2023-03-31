import Exceptions


class Application:

    def __init__(self):
        self.users = []

    def create_user(self, email, password):
        if self.exists(email):
            raise Exceptions.UserAlreadyExistsException

        new_user = User()
        new_user.set_email(email)
        new_user.set_password(password)
        self.users.append(new_user)

    def find_user(self, email):
        found = [user for user in self.users if user.email == email]
        if not found:
            raise Exceptions.UserDoesNotExistsException
        else:
            return found[0]

    def exists(self, email):
        try:
            return bool(self.find_user(email))
        except Exceptions.UserDoesNotExistsException:
            return False

    def remove_user(self, email):
        if self.exists(email):
            list_of_matched = [matched for matched in self.users if matched.email == email]
            for user in list_of_matched:
                self.users.remove(user)
        else:
            raise Exceptions.UserDoesNotExistsException


class User:
    def __init__(self):
        self.email = None
        self.__password = None

    def set_email(self, email):
        if email == '' or email is None:
            raise Exceptions.EmptyFieldException()

        self.email = email

    def set_password(self, password):
        if password == '' or password is None:
            raise Exceptions.EmptyFieldException()

        self.__password = password
