
from domain.interface_adapters.repositories import pets_repository as pr


class AddOne(object):
    """
    Addone new Pet use case
    """

    def __init__(self, petsrepository: pr.PetsRepository):
        self._petsrepo = petsrepository

    def execute(self, item):
        """
        execute add one use case
        Params:
            item (dict): pet item
        Returns:
            (dict): created item
        """
        self._validate(item)
        return self._petsrepo.addone(item)

    def _validate(self, item: dict):
        pass
