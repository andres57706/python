class PetDal:
    def __init__(self, kind: str, name: str, age: float, id_=None):
        self.kind = kind
        self.name = name
        self.age = age
        self.id = id_
