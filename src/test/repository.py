from src.test.dto import CounterDTO


class CounterRepository:
    _id = 0
    _storage = {}

    @property
    def get_id(self):
        self._id += 1
        return self._id

    @classmethod
    async def select_one(cls, id: int) -> CounterDTO | None:
        return cls._storage.get(id)

    @classmethod
    async def insert_one(cls, counter: CounterDTO) -> CounterDTO:


        return

    @classmethod
    async def update_one(cls, id: int) -> CounterDTO:
        ...
