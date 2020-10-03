from domain.interface_adapters.repositories import pets_repository
from ..models.pet import PetDal
from ..db import PETS


class PetsInMemoryRepository(pets_repository.PetsRepository):
    """
    pets in mmory repository implementation
    """

    def getall_and_count(self, limit, offset):
        """[summary]

        Args:
            limit ([type]): [description]
            offset ([type]): [description]

        Returns:
            [tuple(list, int)]: returns a tuple with the fetched items and the items count
        """
        if offset > 0:
            out = PETS[offset: limit]
        else:
            out = PETS[:limit]
        return out, len(PETS)

    def addone(self, item: dict):
        new = PetDal(item['kind'], item['name'],
                     item['age'], self._getnextid())
        PETS.append(new.__dict__)
        return new.__dict__

    def _getnextid(self):
        lastitem = PETS[len(PETS) - 1]
        return lastitem['id'] + 1
