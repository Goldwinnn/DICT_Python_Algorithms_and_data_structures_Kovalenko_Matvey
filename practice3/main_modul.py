class Rebbit:
    """All methods specific to rabbits"""
    name: str  # rabbit name
    breed: str  # rabbit breed
    areal: str  # rabbit habitat
    size: int  # rabbit size in kilograms
    color: str  # rabbit color

    def __init__(self, name: str, breed: str, areal: str, size: int, color: str) -> None:
        """Constructor of the class to set up all basic variables"""
        self.name = name
        self.breed = breed
        self.areal = areal
        self.size = int(size)
        self.color = color


    def generate_message(self) -> str:
        """Generate a message describing the rabbit"""
        size_category = self.determine_size()
        areal_category = self.determine_areal()
        message = f"кролик {self.name} має забарвлення {self.color}, {size_category} розмір вагою {self.size} кг " \
                  f"і відноситься до породи {self.breed}, які живуть у {areal_category} регіоні."
        return message
