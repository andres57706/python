import abc


class PetsRepository(abc.ABC):
    """
    pets repository interface
    """

    @abc.abstractmethod
    def getall_and_count(self, limit: int, offset: int):
        """
        get all records and count
        """
        raise NotImplementedError

    def addone(self, item):
        """
        add new pet
        """
        raise NotImplementedError
