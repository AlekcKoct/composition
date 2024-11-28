
# Задание: Применение Принципа Открытости/Закрытости (Open/Closed Principle) в Разработке Простой Игры
#
# Цель: Цель этого домашнего задание - закрепить понимание и навыки применения принципа открытости/закрытости
# (Open/Closed Principle), одного из пяти SOLID принципов объектно-ориентированного программирования.
# Принцип гласит, что программные сущности (классы, модули, функции и т.д.) должны быть открыты для расширения,
# но закрыты для модификации.
#
# Задача: Разработать простую игру, где игрок может использовать различные типы оружия для борьбы с монстрами.
# Программа должна быть спроектирована таким образом, чтобы легко можно было добавлять новые типы оружия,
# не изменяя существующий код бойцов или механизм боя.

from abc import ABC, abstractmethod

# Абстрактный класс Weapon
class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass

# Класс "Конкретный вид оружия 'Меч'"
class Sword(Weapon):
    def attack(self):
        return "Воин наносит удар мечом."

# Класс "Конкретный вид оружия 'Лук'"
class Bow(Weapon):
    def attack(self):
        return "Воин наносит удар из лука."

# Класс Воин(Warrior)
class Warrior:
    def __init__(self, name):
        self.name = name
        self.weapon = None

    def change_weapon(self, weapon):
        self.weapon = weapon
        print(f"{self.name} выбирает новое оружие.")

    def attack(self):
        if self.weapon:
            print(self.weapon.attack())
        else:
            print(f"{self.name} не вооружен.")

# Класс Враг(Enemy)
class Enemy:
    def __init__(self, name):
        self.name = name

    def defeat(self):
        print(f"{self.name} побежден!")

# Пример использования этой игры
fighter = Warrior("Воин")
enemy = Enemy("Враг")

sword = Sword()
fighter.change_weapon(sword)
fighter.attack()
enemy.defeat()

