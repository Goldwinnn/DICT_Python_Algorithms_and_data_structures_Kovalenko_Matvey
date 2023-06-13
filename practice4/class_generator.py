import random
from class_rabbit import Rabbit


class Generator:
    def __init__(self):
        self.name_list = ["Єва", "Дарсі", "Поллі", "Макс", "Боня", "Бетті", "Венера", "Гретта", "Евгеща", "Джек"]
        self.breed_list = ["Фладнр", "Полтавське серебро", "Гермалин", "Мини рекс", "Тан"]
        self.color_list = ["Північна та Південна Америка", "Європа та Азія", "Африка", "Австралія"]
        self.areal_list = ["Рудий", "Чорний", "Білий", "Сірий", "Коричневий"]

    def generate_rabbit(self) -> Rabbit:
        name = random.choice(self.name_list)
        breed = random.choice(self.breed_list)
        areal = random.choice(self.areal_list)
        size = random.randint(10, 100)
        color = random.choice(self.color_list)
        rabbit = Rabbit(name, breed, areal, size, color)
        return rabbit

    def generate_rabbit_list(self, count: int) -> list:
        rabbit_list = [self.generate_rabbit() for _ in range(count)]
        return rabbit_list


# Create a random rabbit
random_rabbit = Generator().generate_rabbit()

# Print a message about the random rabbit
message = random_rabbit.generate_message()
print(message)
