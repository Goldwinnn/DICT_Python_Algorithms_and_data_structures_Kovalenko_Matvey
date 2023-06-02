import random
from typing import List


class Rabbit:
    def __init__(self, name: str, breed: str, areal: str, size: int, color: str):
        self.name = name
        self.breed = breed
        self.areal = areal
        self.size = size
        self.color = color

    def determine_size_category(self) -> str:
        if self.size > 7:
            return "дуже великий"
        elif self.size > 5:
            return "великий"
        elif self.size > 4:
            return "середній"
        else:
            return "невеликий"

    def determine_areal_category(self) -> str:
        if self.areal == "Північна та Південна Америка":
            return "американському"
        elif self.areal == "Європа та Азія":
            return "євроазіатському"
        elif self.areal == "Африка":
            return "африканському"
        elif self.areal == "Австралія":
            return "австралійському"
        else:
            return "невідомому"

    def generate_message(self) -> str:
        size_category = self.determine_size_category()
        areal_category = self.determine_areal_category()
        message = f"Кролик {self.name} має забарвлення {self.color}, {size_category} розмір вагою {self.size} кг " \
                  f"і відноситься до породи {self.breed}, які живуть у {areal_category} регіоні."
        return message

class Generator:
    @staticmethod
    def generate_rabbit() -> Rabbit:
        names = ["Буцім", "Мак", "Харт", "Фредді", "Санчо", "Багіра", "Рейн", "Роксі", "Смокі", "Джек"]
        breeds = ["Білий Велетень", "Рекс", "Полтавське Серебро", "Т-Рекс", "Фландр"]
        areals = ["Північна та Південна Америка", "Європа та Азія", "Африка", "Австралія"]
        colors = ["чорний", "коричневий", "білий", "сірий", "рудий"]

        # Generate random values for each rabbit property
        name = random.choice(names)
        breed = random.choice(breeds)
        areal = random.choice(areals)
        size = random.randint(1, 10)
        color = random.choice(colors)

        # Create a Rabbit object with random properties
        rabbit = Rabbit(name, breed, areal, size, color)
        return rabbit

# Generate a random rabbit
random_rabbit = Generator.generate_rabbit()

# Print the message about the random rabbit
message = random_rabbit.generate_message()
print(message)


def generate_1000() -> List[Rabbit]:
    rabbits = [Generator.generate_rabbit() for _ in range(1000)]
