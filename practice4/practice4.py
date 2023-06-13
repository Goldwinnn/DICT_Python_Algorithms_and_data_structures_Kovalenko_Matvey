from collections.abc import Iterable
import copy
from abstractstructure import AbstractStructureBasic


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class RabbitListBasic(AbstractStructureBasic):
    def __init__(self, *args: Iterable):
        self._head = None
        self._tail = None
        self._length = 0
        for rabbit in args:
            self.append(rabbit)

    def __len__(self) -> int:
        return self._length

    def __repr__(self) -> str:
        result = []
        current = self._head
        while current is not None:
            result.append(repr(current.value))
            current = current.next
        return ', '.join(result)

    def __getitem__(self, key):
        if not 0 <= key < len(self):
            raise IndexError("Index out of range")
        current = self._head
        for _ in range(key):
            current = current.next
        return current.value

    def __setitem__(self, key, value):
        if not 0 <= key < len(self):
            raise IndexError("Index out of range")
        current = self._head
        for _ in range(key):
            current = current.next
        current.value = value

    def append(self, value):
        new_node = Node(value)
        if self._tail is None:
            self._head = new_node
            self._tail = new_node
        else:
            self._tail.next = new_node
            self._tail = new_node
        self._length += 1

    def insert(self, index, value):
        if index == 0 or index == len(self):
            self.append(value)
        else:
            current = self._head
            for _ in range(index - 1):
                current = current.next
            new_node = Node(value)
            new_node.next = current.next
            current.next = new_node
            self._length += 1

    def index(self, value, start=0, stop=-1):
        if stop == -1:
            stop = len(self)
        current = self._head
        for i in range(start, stop):
            if current.value == value:
                return i
            current = current.next
        raise ValueError("Value not found")

    def remove(self, value):
        if self._head is None:
            raise ValueError("Value not found")

        if self._head.value == value:
            self._head = self._head.next
            if self._head is None:
                self._tail = None
            self._length -= 1
            return

        prev_node = self._head
        node = self._head.next

        while node is not None and node.value != value:
            prev_node = node
            node = node.next

        if node is None:
            raise ValueError("Value not found")

        prev_node.next = node.next

        if prev_node.next is None:
            self._tail = prev_node

        self._length -= 1


class RabbitListExtended(RabbitListBasic):

    def __init__(self, *args: Iterable):
        super().__init__(*args)

    def clear(self):
        self._length = 0
        self._head = None
        self._tail = None

    def copy(self):
        return list(self)

    def __iter__(self):
        self._current_node = self._head
        return self

    def __next__(self):
        if self._current_node is None:
            raise StopIteration
        else:
            current_value = self._current_node.value
            self._current_node = self._current_node.next
            return current_value

    def __delitem__(self, key):
        if not 0 <= key < self._length:
            raise IndexError("Index out of range")
        if key == 0:
            self._head = self._head.next
        else:
            prev_node = self._head
            current_node = self._head.next
            for i in range(key - 1):
                prev_node = current_node
                current_node = current_node.next
            prev_node.next = current_node.next
            if prev_node.next is None:
                self._tail = prev_node

        self._length -= 1

    def extend(self, values: Iterable):
        for value in values:
            self.append(value)

    def pop(self, index):
        if not 0 <= index < self._length:
            raise IndexError("Index out of range")
        if index == 0:
            popped_value = self._head.value
            self._head = self._head.next
        else:
            prev_node = self._head
            current_node = self._head.next
            for i in range(index - 1):
                prev_node = current_node
                current_node = current_node.next
            popped_value = current_node.value
            prev_node.next = current_node.next
            if prev_node.next is None:
                self._tail = prev_node

        self._length -= 1
        return popped_value

    def reverse(self):
        prev_node = None
        current_node = self._head
        while current_node is not None:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
        self._head = prev_node

    def count(self, value):
        count = 0
        current_node = self._head
        while current_node is not None:
            if current_node.value == value:
                count += 1
            current_node = current_node.next
        return count


class RabbitListBonus(RabbitListExtended):
    def append(self, value):
        new_node = Node(value)
        if self._tail is None:
            self._head = new_node
            self._tail = new_node
        else:
            self._tail.next = new_node
            self._tail = new_node
        self._length += 1

    def deepcopy(self):
        new_list = RabbitListBonus()
        current_node = self._head
        while current_node is not None:
            new_list.append(copy.deepcopy(current_node.value))
            current_node = current_node.next
        return new_list

    def min(self):
        if self._head is None:
            raise ValueError("the list is empty")
        min_rabbit = self._head.value
        current_node = self._head.next
        while current_node is not None:
            if current_node.value < min_rabbit:
                min_rabbit = current_node.value
            current_node = current_node.next
        return min_rabbit

    def max(self):
        if self._head is None:
            raise ValueError("the list is empty")
        max_rabbit = self._head.value
        current_node = self._head.next
        while current_node is not None:
            if current_node.value > max_rabbit:
                max_rabbit = current_node.value
            current_node = current_node.next
        return max_rabbit

    def __add__(self, other):
        if not isinstance(other, RabbitListBonus):
            raise TypeError("Expected object of type RabbitListBonus")
        new_list = RabbitListBonus()
        current_node = self._head
        while current_node is not None:
            new_list.append(copy.deepcopy(current_node.value))
            current_node = current_node.next
        current_node = other._head
        while current_node is not None:
            new_list.append(copy.deepcopy(current_node.value))
            current_node = current_node.next
        return new_list

    def __mul__(self, other):
        if not isinstance(other, int):
            raise TypeError("Expected an integer")
        if other < 0:
            raise ValueError("Number should be non-negative")
        new_list = RabbitListBonus()
        for _ in range(other):
            current_node = self._head
            while current_node is not None:
                new_list.append(copy.deepcopy(current_node.value))
                current_node = current_node.next
        return new_list

class Rabbit:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'Rabbit({self.name})'


def main():
    rabbits = RabbitListBonus()
    rabbits.append(Rabbit("Bob"))
    rabbits.append(Rabbit("Alice"))
    rabbits.append(Rabbit("Charlie"))
    print(rabbits)
    rabbits.reverse()
    print(rabbits)

if __name__ == '__main__':
    main()
