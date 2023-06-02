class Rebbit:
    def __init__(self, name, breed, areal, size, color):
        self.name = name
        self.breed = breed
        self.areal = areal
        self.size = int(size)
        self.color = color

    def determine_size(self):
        if self.size > 5-7:
            return "дуже великий"
        elif self.size > 4-5:
            return "великий"
        elif self.size > 3-4:
            return "середній"
        else:
            return "невеликий"

    def determine_areal(self):
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

    def generate_message(self):
        size_category = self.determine_size()
        areal_category = self.determine_areal()
        message = f"кролик {self.name} має забарвлення {self.color}, {size_category} розмір довжиною {self.size} кг " \
                  f"і відноситься до породи {self.breed}, які живуть у {areal_category} регіоні."
        return message


# Запрос данных у пользователя
name = input("Введіть ім'я кролика: ")
breed = input("Введіть породу кролик: ")
areal = input("Введіть регіон кролика (Північна та Південна Америка, Європа та Азія, Африка, Австралія): ")
size = input("Введіть розмір кролика (кг): ")
color = input("Введіть забарвлення кролика: ")

# Створення об'єкту класу rebbit
rebbit = Rebbit(name, breed, areal, size, color)

# Вивід повідомлення про кролка
message = rebbit.generate_message()
print(message)
