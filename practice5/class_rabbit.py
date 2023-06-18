class Rabbit:
    def __init__(self, name, breed, color, size, areal):
        self.name = name
        self.breed = breed
        self.color = color
        self.size = size
        self.areal = areal

    def get_info(self):
        return f"Rabbit({self.name}, {self.breed}, {self.color}, {self.size}, {self.areal})"

    def __repr__(self):
        return f"Rabbit({self.name}, {self.breed}, {self.color}, {self.size}, {self.areal})"

    def determine_size_category(self):
        if self.size > 7:
            return "large"
        elif self.size > 5-7:
            return "medium"
        elif self.size > 3-5:
            return "small"
        else:
            return "tiny"

    def determine_areal_category(self):
        areal_categories = {
            "North and South America": "American",
            "Europe and Asia": "Euro-Asian",
            "Africa": "African",
            "Australia": "Australian"
        }
        return areal_categories.get(self.areal, "unknown")

    def generate_message(self):
        size_category = self.determine_size_category()
        areal_category = self.determine_areal_category()
        message = f"The rabbit {self.name} of breed {self.breed}, living in the {areal_category} region, has a {size_category} size, " \
                  f"measuring {self.size} kg, and has {self.color} coloration."
        return message
