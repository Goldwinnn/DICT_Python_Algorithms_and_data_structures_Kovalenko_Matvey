import pytest
from class_rabbit import Rabbit
from abstractlimitstructure_p5 import Stack, PriorQueue


class TestStack:
    def test_push_pop(self):
        stack = Stack()
        rabbit1 = Rabbit("Rabbit1", "Breed1", "Color1", 1, 4)
        rabbit2 = Rabbit("Rabbit2", "Breed2", "Color2", 2, 5)
        rabbit3 = Rabbit("Rabbit3", "Breed3", "Color3", 3, 3)
        stack.push(rabbit1)
        stack.push(rabbit2)
        stack.push(rabbit3)
        assert stack.pop() == rabbit3
        assert stack.pop() == rabbit2
        assert stack.pop() == rabbit1

    def test_pop_empty_stack(self):
        stack = Stack()
        with pytest.raises(IndexError):
            stack.pop()

    def test_top(self):
        stack = Stack()
        with pytest.raises(IndexError):
            stack.top()
        rabbit1 = Rabbit("Rabbit1", "Breed1", "Color1", 1, 4)
        stack.push(rabbit1)
        assert stack.top() == rabbit1

    def test_len(self):
        stack = Stack()
        assert len(stack) == 0
        rabbit1 = Rabbit("Rabbit1", "Breed1", "Color1", 1, 4)
        stack.push(rabbit1)
        assert len(stack) == 1

    def test_repr(self):
        stack = Stack()
        rabbit1 = Rabbit("Rabbit1", "Breed1", "Color1", 1, 4)
        rabbit2 = Rabbit("Rabbit2", "Breed2", "Color2", 2, 5)
        stack.push(rabbit1)
        stack.push(rabbit2)
        expected_repr = (
            "[Rabbit(Rabbit2, Breed2, Color2, 2, 5), Rabbit(Rabbit1, Breed1, Color1, 1, 4)]"
        )
        assert repr(stack) == expected_repr


class TestPriorQueue:
    def test_enqueue_dequeue(self):
        queue = PriorQueue()
        rabbit1 = Rabbit("Rabbit1", "Breed1", "Color1", 1, 4)
        rabbit2 = Rabbit("Rabbit2", "Breed2", "Color2", 2, 5)
        rabbit3 = Rabbit("Rabbit3", "Breed3", "Color3", 3, 3)
        queue.enqueue(rabbit1)
        queue.enqueue(rabbit2)
        queue.enqueue(rabbit3)
        assert queue.dequeue().size == 3

    def test_dequeue_empty_queue(self):
        queue = PriorQueue()
        with pytest.raises(IndexError):
            queue.dequeue()

    def test_is_empty(self):
        queue = PriorQueue()
        assert queue.is_empty()
        rabbit1 = Rabbit("Rabbit1", "Breed1", "Color1", 1, 4)
        queue.enqueue(rabbit1)
        assert not queue.is_empty()

    def test_size(self):
        queue = PriorQueue()
        assert queue.size() == 0
        rabbit1 = Rabbit("Rabbit1", "Breed1", "Color1", 1, 4)
        queue.enqueue(rabbit1)
        assert queue.size() == 1

    def test_peek(self):
        queue = PriorQueue()
        with pytest.raises(IndexError):
            queue.peek()
        rabbit1 = Rabbit("Rabbit1", "Breed1", "Color1", 1, 4)
        queue.enqueue(rabbit1)
