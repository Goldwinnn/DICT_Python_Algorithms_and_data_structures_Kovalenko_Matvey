import random


class Rabbit:
    def __init__(self, name, breed, color, weight):
        self.name = name
        self.breed = breed
        self.color = color
        self.weight = weight

    def generate_message(self):
        return f"This is {self.name}, a {self.color} {self.breed} rabbit weighing {self.weight} pounds."


class Generator:
    NAME_LIST = ["Fluffy", "Bunny", "Thumper", "Cotton", "Hopper", "Nibbles", "Snowball", "Whiskers", "Coco", "Oreo"]
    BREED_LIST = ["Dutch", "Lop", "Rex", "Flemish Giant", "Angora"]
    COLOR_LIST = ["White", "Brown", "Black", "Gray", "Spotted"]
    WEIGHT_RANGE = (1, 10)

    @staticmethod
    def generate_rabbit() -> Rabbit:
        name = random.choice(Generator.NAME_LIST)
        breed = random.choice(Generator.BREED_LIST)
        color = random.choice(Generator.COLOR_LIST)
        weight = random.uniform(*Generator.WEIGHT_RANGE)
        rabbit = Rabbit(name, breed, color, weight)
        return rabbit

    def generate_1000(self) -> list:
        rabbit_list = [self.generate_rabbit() for _ in range(1000)]
        return rabbit_list

    def generate_10000(self) -> list:
        rabbit_list = [self.generate_rabbit() for _ in range(10000)]
        return rabbit_list

    def generate_single(self) -> list:
        rabbit_list = [self.generate_rabbit()]
        return rabbit_list


# Create a random rabbit
random_rabbit = Generator().generate_rabbit()

# Display a message about the random rabbit
message = random_rabbit.generate_message()
print(message)


def abstract_object():
    return None
