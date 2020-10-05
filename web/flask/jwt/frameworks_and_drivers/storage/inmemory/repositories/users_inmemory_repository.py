from domain.interface_adapters.repositories import users_repository as usrepo
from ..db import USERS


class UsersInMemoryRepository(usrepo.UsersRepository):
    """
    Users in memory repository implementation
    """

    def __init__(self):
        super().__init__()

    def add(self, item):
        item['id'] = self._getnextid()
        USERS.append(item)
        return item

    def get_by_email(self, email):
        return next(list(filter(lambda u: u['email'] == email, USERS)), None)

    def _getnextid(self):
        lastitem = USERS[len(USERS) - 1]
        return lastitem['id'] + 1
