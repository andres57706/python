from domain.interface_adapters.repositories import users_repository as usrepo


class SignIn(object):
    """
    Signin use case
    """

    def __init__(self, users_repository: usrepo.UsersRepository):
        self._usersrepo = users_repository

    def execute(self, email, password):
        """
        executes the signin use case

        Params:
            email [str]: email address
            password [str]: user's password
        """
        pass
