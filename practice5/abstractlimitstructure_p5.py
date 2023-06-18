from abc import ABC, abstractmethod


class AbstractStack(ABC):
    @abstractmethod
    def push(self, value):
        pass

    @abstractmethod
    def pop(self):
        pass

    @abstractmethod
    def top(self):
        pass

    @abstractmethod
    def __len__(self):
        pass


class PriorityQueue(ABC):
    @abstractmethod
    def enqueue(self, value):
        pass

    @abstractmethod
    def dequeue(self):
        pass

    @abstractmethod
    def is_empty(self):
        pass

    @abstractmethod
    def size(self):
        pass

    @abstractmethod
    def peek(self):
        pass


class Rabbit:
    def __init__(self, name, breed, color, age, size):
        self.name = name
        self.breed = breed
        self.color = color
        self.age = age
        self.size = size

    def __repr__(self):
        return f"Rabbit({self.name}, {self.breed}, {self.color}, {self.age}, {self.size})"


class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node


class Stack(AbstractStack):
    def __init__(self):
        self._top = None
        self._size = 0

    def push(self, value):
        new_node = Node(value)
        new_node.next_node = self._top
        self._top = new_node
        self._size += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        node_to_remove = self._top
        self._top = self._top.next_node
        self._size -= 1
        return node_to_remove.value

    def top(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self._top.value

    def __len__(self):
        return self._size


class PriorQueue(PriorityQueue):
    def __init__(self):
        self._head = None

    def enqueue(self, value):
        new_node = Node(value)
        if self.is_empty() or value.size > self._head.value.size:
            new_node.next_node = self._head
            self._head = new_node
        else:
            current = self._head
            while current.next_node is not None and value.size <= current.next_node.value.size:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        dequeued_node = self._head
        self._head = self._head.next_node
        return dequeued_node.value

    def is_empty(self):
        return self._head is None

    def size(self):
        count = 0
        current = self._head
        while current is not None:
            count += 1
            current = current.next_node
        return count

    def peek(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self._head.value
