
from domain.interface_adapters.repositories import pets_repository as pr


class GetAll(object):
    """
    Get all pets use case
    """

    def __init__(self, petsrepository: pr.PetsRepository):
        self._petsrepo = petsrepository

    def execute(self, limit=10, offset=0):
        """
        executes get all pets use case

        Params:
            limit [int]: records to fetch
            offset [int]: offset value to move around the records set
        Returns:
            (tuple): Returns a tuple (items: list, count: int)
        """
        if limit > 1000:
            raise Exception(
                'We can not deliver too many records, max aloowed 1000.')
        if offset < 0:
            raise 'offset para must be positive'
        limit = 10 if limit == 0 else limit
        return self._petsrepo.getall_and_count(limit, offset)
