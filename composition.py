
# Базовый(основной) класс Animal
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Подкласс Bird
class Bird(Animal):
    def make_sound(self):
        return f"{self.name} издает звук: Поет!"


# Подкласс Mammal
class Mammal(Animal):
    def make_sound(self):
        return f"{self.name} издает звук: Рычит!"


# Подкласс Reptile
class Reptile(Animal):
    def make_sound(self):
        return f"{self.name} издает звук: Шипит!"


def animal_sound(animals):
    for animal in animals:
        print(animal.make_sound())


# Класс Zoo
class Zoo:
    def __init__(self):
        self.animals = []
        self.employees = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def add_employee(self, employee):
        self.employees.append(employee)

    def show_animals(self):
        for animal in self.animals:
            if animal.name == "Канарейка":
                print(f"Птпчка: {animal.name}, Возраст: {animal.age}")
            else:
                print(f"Животное: {animal.name}, Возраст: {animal.age}")


# Класс ZooKeeper
class ZooKeeper:
    def __init__(self, name):
        self.name = name

    def feed_animal(self, animal):
        if lion != "":
            animal.name = "Льва"
            return f"{self.name} кормит {animal.name}."
        else:
            return f"{self.name} кормит {animal.name}."


# Класс Veterinarian
class Veterinarian:
    def __init__(self, name):
        self.name = name

    def heal_animal(self, animal):
        if snake != "":
            animal.name = "Удава"
            return f"{self.name} лечит {animal.name}."
        else:
            return f"{self.name} лечит {animal.name}."


class Kinder:
    def __init__(self, name):
        self.name = name

    def kind_animal(self, animal):
        if parrot != "":
            animal.name = "Канарейку"
            return f"{self.name} смотрят {animal.name}."
        else:
            return f"{self.name} смотрят {animal.name}."


# Пример использования классов
if __name__ == "__main__":
    # Создаем животных
    parrot = Bird("Канарейка", "2 года")
    lion = Mammal("Лев", "5 лет")
    snake = Reptile("Удав", "3 года")


    # Создаем зоопарк и добавляем животных
    zoo = Zoo()
    zoo.add_animal(parrot)
    zoo.add_animal(lion)
    zoo.add_animal(snake)

    # Создаем сотрудников зоопарка
    zookeeper = ZooKeeper("Охранник Вася")
    veterinarian = Veterinarian("Ветеринар")
    kinder = Kinder("Дети")

    # Добавляем сотрудников в зоопарк
    zoo.add_employee(zookeeper)
    zoo.add_employee(veterinarian)


    # Показываем информацию о животных в зоопарке
    print("\nЖивотные и птицы в зоопарке:")
    zoo.show_animals()

    # Демонстрируем звуки животных
    print("\nЗвуки животных и птиц:")
    animal_sound(zoo.animals)

    # Демонстрируем действия сотрудников
    print("\nДействия сотрудников в зоопарке:")
    print(zookeeper.feed_animal(lion))
    print(veterinarian.heal_animal(snake))
    print(kinder.kind_animal(parrot))

