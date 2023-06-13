from list_extra import CustomList


class UniqueList(CustomList):
    def __init__(self):
        super().__init__()
        self.unique_values = set()

    def append(self, value):
        self._check_duplicate(value)
        super().append(value)
        self.unique_values.add(value)

    def insert(self, index, value):
        self._check_duplicate(value)
        super().insert(index, value)
        self.unique_values.add(value)

    def _check_duplicate(self, value):
        if value in self.unique_values:
            raise ValueError("Value already exists in the list!")
