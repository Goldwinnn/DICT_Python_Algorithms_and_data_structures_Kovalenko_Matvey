import pytest
from class_rabbit import Rabbit
from practice4 import RabbitListBasic, RabbitListExtended


class TestRabbitListBasic:
    def setup_method(self):
        self.rabbit1 = Rabbit("Rabbit1", "Breed1", "Color1", 1, 4)
        self.rabbit2 = Rabbit("Rabbit2", "Breed2", "Color2", 2, 5)
        self.rabbit3 = Rabbit("Rabbit3", "Breed3", "Color3", 3, 6)

    def test_append_and_getitem(self):
        rabbit_list = RabbitListBasic()
        rabbit_list.append(self.rabbit1)
        rabbit_list.append(self.rabbit2)
        rabbit_list.append(self.rabbit3)
        assert rabbit_list[0] == self.rabbit1
        assert rabbit_list[1] == self.rabbit2
        assert rabbit_list[2] == self.rabbit3
        with pytest.raises(IndexError):
            assert rabbit_list[3]

    def test_len(self):
        rabbit_list = RabbitListBasic()
        rabbit_list.append(self.rabbit1)
        rabbit_list.append(self.rabbit2)
        rabbit_list.append(self.rabbit3)
        assert len(rabbit_list) == 3

    def test_setitem(self):
        rabbit_list = RabbitListBasic()
        rabbit_list.append(self.rabbit1)
        rabbit_list.append(self.rabbit2)
        rabbit_list.append(self.rabbit3)
        rabbit_list[1] = self.rabbit3
        assert rabbit_list[1] == self.rabbit3
        with pytest.raises(IndexError):
            rabbit_list[3] = self.rabbit1

    def test_index(self):
        rabbit_list = RabbitListBasic()
        rabbit_list.append(self.rabbit1)
        rabbit_list.append(self.rabbit2)
        assert rabbit_list.index(self.rabbit2) == 1
        with pytest.raises(ValueError):
            rabbit_list.index(self.rabbit3)

    def test_remove(self):
        rabbit_list = RabbitListBasic()
        rabbit_list.append(self.rabbit1)
        rabbit_list.append(self.rabbit2)
        rabbit_list.append(self.rabbit3)
        rabbit_list.remove(self.rabbit2)
        assert self.rabbit2 not in rabbit_list
        with pytest.raises(ValueError):
            rabbit_list.remove(self.rabbit2)


class TestRabbitListExtended:
    def setup_method(self):
        self.rabbit_list = RabbitListExtended()
        self.rabbit1 = Rabbit("Rabbit1", "Breed1", "Color1", 1, 4)
        self.rabbit2 = Rabbit("Rabbit2", "Breed2", "Color2", 2, 3)
        self.rabbit3 = Rabbit("Rabbit3", "Breed3", "Color3", 3, 2)

    def test_clear(self):
        self.rabbit_list.append(self.rabbit1)
        self.rabbit_list.append(self.rabbit2)
        self.rabbit_list.clear()
        assert len(self.rabbit_list) == 0
        assert self.rabbit_list.head is None
        assert self.rabbit_list.tail is None

    def test_extend(self):
        self.rabbit_list.append(self.rabbit1)
        self.rabbit_list.append(self.rabbit2)
        self.rabbit_list.extend([self.rabbit3])
        assert len(self.rabbit_list) == 4
        assert self.rabbit_list[1] == self.rabbit1
        assert self.rabbit_list[2] == self.rabbit2
        assert self.rabbit_list[3] == self.rabbit3
