from frameworks_and_drivers.storage.inmemory.repositories \
    import pets_inmemory_repository as petsinmemorepo

from .add_one import AddOne
from .get_all import GetAll
_petsrepo = petsinmemorepo.PetsInMemoryRepository()

# add one pets use case
add_one = AddOne(_petsrepo).execute
# get all pets use case
get_all = GetAll(_petsrepo).execute
