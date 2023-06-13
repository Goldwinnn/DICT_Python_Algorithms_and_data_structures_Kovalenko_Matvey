import random
from main_modul import Rebbit


class Generator:
    NAMES = ["Hoppy", "Thumper", "Bunny", "Cotton", "Fluffy", "Nibbles", "Hopper", "Pippin", "Whiskers", "Snowball"]
    BREEDS = ["Holland Lop", "Netherland Dwarf", "Lionhead", "Flemish Giant", "Mini Rex", "Dutch", "Mini Lop", "Angora", "Jersey Wooly"]
    CATEGORIES = ["Pet", "Show"]
    AREALS = ["North America", "Europe", "Asia", "Australia"]
    COLORS = ["White", "Brown", "Black", "Gray", "Spotted"]

    @staticmethod
    def generate_rebbit() -> Rebbit:
        name = random.choice(Generator.NAMES)
        breed = random.choice(Generator.BREEDS)
        category = random.choice(Generator.CATEGORIES)
        areal = random.choice(Generator.AREALS)
        weight = round(random.uniform(0.5, 5), 2)  # weight in kilograms
        color = random.choice(Generator.COLORS)
        rebbit = Rebbit(name, breed, category, areal, weight, color)
        return rebbit

    def generate_n_rebbits(self, n: int) -> list:
        return [self.generate_rebbit() for _ in range(n)]


# Create a random rebbit
random_rebbit = Generator.generate_rebbit()

# Print information about the random rebbit
message = random_rebbit.generate_message()
print(message)

# Generate a list of 1000 random rebbits
generator = Generator()
rebbit_list_1000 = generator.generate_n_rebbits(1000)

# Generate a list of 10000 random rebbits
rebbit_list_10000 = generator.generate_n_rebbits(10000)
