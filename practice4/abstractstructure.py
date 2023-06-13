from abc import ABC, abstractmethod
from collections.abc import Iterable
from class_rabbit import Rabbit


class AbstractStructureBasic(ABC):

    @abstractmethod
    def __init__(self, *args: Iterable[Rabbit]):
        pass

    @abstractmethod
    def __len__(self) -> int:
        pass

    @abstractmethod
    def __repr__(self) -> str:
        pass

    @abstractmethod
    def __getitem__(self, key) -> Rabbit:
        pass

    @abstractmethod
    def __setitem__(self, key, value):
        pass

    @abstractmethod
    def append(self, value: Rabbit) -> None:
        pass

    @abstractmethod
    def insert(self, index: int, value: Rabbit) -> None:
        pass

    @abstractmethod
    def index(self, value: Rabbit, start: int = 0, stop: int = -1) -> int:
        pass

    @abstractmethod
    def remove(self, value: Rabbit) -> None:
        pass
