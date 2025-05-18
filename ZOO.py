
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        print("Some generic animal sound")

    def eat(self):
        print(f"{self.name} is eating.")



class Mammal(Animal):
    def __init__(self, name, age, fur_color):
        super().__init__(name, age)
        self.fur_color = fur_color

    def make_sound(self):
        print(f"{self.name} says: Roar!")



class Giraffe(Mammal):
    def __init__(self, name, age, fur_color, height):
        super().__init__(name, age, fur_color)
        self.height = height

    def make_sound(self):
        print(f"{self.name} says: Mooooo!")

    def stretch_neck(self):
        print(f"{self.name} stretches its long neck.")



class Hippopotamus(Mammal):
    def __init__(self, name, age, fur_color):
        super().__init__(name, age, fur_color)

    def make_sound(self):
        print(f"{self.name} says: Grunt-grunt!")

    def swim(self):
        print(f"{self.name} splashes in the water.")



class ZooKeeper:
    def __init__(self, name):
        self.name = name

    def feed_animal(self, animal):
        print(f"{self.name} ухаживает и кормит {animal.name}.")



class Veterinarian:
    def __init__(self, name):
        self.name = name

    def heal_animal(self, animal):
        print(f"{self.name} лечит животное: {animal.name}.")



class Zoo:
    def __init__(self, name):
        self.name = name
        self.animals = []
        self.staff = []

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"{animal.name} добавлен(а) в зоопарк {self.name}.")

    def add_staff(self, employee):
        self.staff.append(employee)
        print(f"{employee.name} принят(а) на работу в зоопарк {self.name}.")

    def show_animals(self):
        print(f"Животные в зоопарке '{self.name}':")
        for animal in self.animals:
            print(f"- {animal.name}, возраст: {animal.age}")

    def show_staff(self):
        print(f"Сотрудники зоопарка '{self.name}':")
        for employee in self.staff:
            print(f"- {employee.name}")



if __name__ == "__main__":
    # Создаем зоопарк
    my_zoo = Zoo("Зоопарк 'Дикие Звери'")


    giraffe = Giraffe(name="Жирафа", age=6, fur_color="желто-коричневый", height=5.2)


    hippo = Hippopotamus(name="Бегемотик", age=10, fur_color="серый")


    zookeeper_vasya = ZooKeeper(name="Вася")
    vet_stepanych = Veterinarian(name="Степаныч")


    my_zoo.add_animal(giraffe)
    my_zoo.add_animal(hippo)
    my_zoo.add_staff(zookeeper_vasya)
    my_zoo.add_staff(vet_stepanych)


    my_zoo.show_animals()
    my_zoo.show_staff()


    zookeeper_vasya.feed_animal(giraffe)


    vet_stepanych.heal_animal(hippo)