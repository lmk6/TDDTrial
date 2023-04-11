
class EmptyFieldException(Exception):
    def __init__(self):
        super().__init__()


class UserAlreadyExistsException(Exception):
    def __init__(self):
        super().__init__()


class UserDoesNotExistsException(Exception):
    def __init__(self):
        super().__init__()
