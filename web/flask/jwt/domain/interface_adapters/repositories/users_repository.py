from abc import ABC


class UsersRepository(ABC):
    """
    Users repository interface adapter
    """

    def add(self, item):
        """
        Add new user

        Params:
            item [dict]: user item object
        """
        raise NotImplementedError

    def get_by_email(self, email):
        """
        Get user by email

        Params:
            email [str]: email address
        """
        raise NotImplementedError
