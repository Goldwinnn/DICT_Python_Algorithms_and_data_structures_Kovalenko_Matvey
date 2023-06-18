from abc import ABC, abstractmethod
from class_rabbit import Rabbit


class AbstractStack(ABC):
    @abstractmethod
    def push(self, value: Rabbit) -> None:
        pass

    @abstractmethod
    def pop(self) -> Rabbit:
        pass

    @abstractmethod
    def top(self) -> Rabbit:
        pass

    @abstractmethod
    def __repr__(self) -> str:
        pass

    @abstractmethod
    def __len__(self) -> int:
        pass


class PriorityQueue(ABC):
    @abstractmethod
    def enqueue(self, value: Rabbit) -> None:
        pass

    @abstractmethod
    def dequeue(self) -> Rabbit:
        pass

    @abstractmethod
    def top(self) -> Rabbit:
        pass

    @abstractmethod
    def __repr__(self) -> str:
        pass

    @abstractmethod
    def __len__(self) -> int:
        pass
