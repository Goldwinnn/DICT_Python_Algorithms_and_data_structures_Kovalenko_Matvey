class Rabbit:
    name: str  # rabbit name
    breed: str  # rabbit breed
    color: str  # rabbit color
    geographic_region: str  # rabbit geographic region
    size: int  # rabbit size in centimeters

    def __init__(self, name: str, breed: str, color: str, size: int, geographic_region: str) -> None:
        self.name = name
        self.breed = breed
        self.color = color
        self.size = size
        self.geographic_region = geographic_region

    def __repr__(self) -> str:
        return f"Rabbit({self.name}, {self.breed}, {self.color}, {self.size}, {self.geographic_region})"

    def determine_size_category(self) -> str:
        if self.size > 7:
            return "великий"
        elif 5 < self.size <= 7:
            return "середній"
        elif 3 < self.size <= 5:
            return "середній"
        else:
            return "невеликий"

    def determine_areal_category(self) -> str:
        areal_categories = {
            "Північна та Південна Америка": "американському",
            "Європа та Азія": "євроазіатському",
            "Африка": "африканському",
            "Австралія": "австралійському"
        }
        return areal_categories.get(self.geographic_region, "невідомому")

    def generate_message(self) -> str:
        size_category = self.determine_size_category()
        areal_category = self.determine_areal_category()
        message = f"Заєць {self.name} породи {self.breed}, що мешкає у {areal_category} регіоні, має {size_category} розмір, " \
                  f"вагою {self.size} кг, та має забарвлення {self.color}."
        return message
