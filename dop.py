import pickle


class Animal:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def make_sound(self):
        print(f"{self.name} издаёт звук.")

    def eat(self, food: str):
        print(f"{self.name} ест {food}.")


class Bird(Animal):
    def __init__(self, name: str, age: int, wing_span: float):
        super().__init__(name, age)
        self.wing_span = wing_span

    def make_sound(self):
        print(f"{self.name} чирикает: «Чиррик-чиррик!»")

    def fly(self):
        print(f"{self.name} летит с размахом крыльев {self.wing_span} см.")


class Mammal(Animal):
    def __init__(self, name: str, age: int, fur_color: str):
        super().__init__(name, age)
        self.fur_color = fur_color

    def make_sound(self):
        print(f"{self.name} издаёт млекопитающий звук: «Гррр!»")

    def nurse_young(self):
        print(f"{self.name} кормит детёнышей молоком.")


class Reptile(Animal):
    def __init__(self, name: str, age: int, scale_type: str):
        super().__init__(name, age)
        self.scale_type = scale_type

    def make_sound(self):
        print(f"{self.name} шипит: «Шшш…»")

    def shed_skin(self):
        print(f"{self.name} сбрасывает {self.scale_type} чешую.")


class ZooKeeper:
    def __init__(self, name: str, experience_years: int):
        self.name = name
        self.experience_years = experience_years

    def feed_animal(self, animal: Animal, food: str):
        print(f"Смотритель {self.name} кормит {animal.name} ({animal.__class__.__name__}) {food}.")
        animal.eat(food)


class Veterinarian:
    def __init__(self, name: str, specialization: str):
        self.name = name
        self.specialization = specialization

    def heal_animal(self, animal: Animal):
        print(f"Ветеринар {self.name} ({self.specialization}) осматривает и лечит {animal.name}.")
        print(f"{animal.name} поправился после лечения!")



class Zoo:
    def __init__(self, name: str):
        self.name = name
        self.animals = []     # список Animal
        self.employees = []   # список ZooKeeper/Veterinarian

    def add_animal(self, animal: Animal):
        self.animals.append(animal)
        print(f"В зоопарк «{self.name}» добавлено животное: {animal.name} ({animal.__class__.__name__}).")

    def add_employee(self, employee):
        self.employees.append(employee)
        print(f"В зоопарк «{self.name}» принят сотрудник: {employee.name} ({employee.__class__.__name__}).")

    def list_animals(self):
        print(f"Животные в зоопарке «{self.name}»:")
        for a in self.animals:
            print(f" - {a.name} ({a.__class__.__name__})")

    def list_employees(self):
        print(f"Сотрудники зоопарка «{self.name}»:")
        for e in self.employees:
            print(f" - {e.name} ({e.__class__.__name__})")

    def save_to_file(self, filename: str):
        """Сохраняет текущее состояние зоопарка в файл."""
        with open(filename, 'wb') as f:
            pickle.dump(self, f)
        print(f"Состояние зоопарка «{self.name}» сохранено в файл '{filename}'.")

    @classmethod
    def load_from_file(cls, filename: str):

        with open(filename, 'rb') as f:
            zoo = pickle.load(f)
        print(f"Состояние зоопарка «{zoo.name}» загружено из файла '{filename}'.")
        return zoo


if __name__ == "__main__":
    import os

    FILENAME = "my_zoo.pickle"


    if os.path.exists(FILENAME):
        my_zoo = Zoo.load_from_file(FILENAME)
    else:

        tweety = Bird(name="Твити", age=1, wing_span=25.0)
        bella  = Mammal(name="Белла", age=4, fur_color="коричневый")
        sly    = Reptile(name="Слай", age=2, scale_type="гладкую")

        keeper = ZooKeeper(name="Иван", experience_years=5)
        vet    = Veterinarian(name="Ольга", specialization="рептилии")

        my_zoo = Zoo(name="Мой Зоопарк")
        my_zoo.add_animal(tweety)
        my_zoo.add_animal(bella)
        my_zoo.add_animal(sly)

        my_zoo.add_employee(keeper)
        my_zoo.add_employee(vet)


        my_zoo.save_to_file(FILENAME)


    print()
    my_zoo.list_animals()
    my_zoo.list_employees()


    print("\n---- Работа сотрудников ----")
    # пусть смотритель и ветеринар работают с первым животным
    if my_zoo.animals and my_zoo.employees:
        keeper = next((e for e in my_zoo.employees if isinstance(e, ZooKeeper)), None)
        vet    = next((e for e in my_zoo.employees if isinstance(e, Veterinarian)), None)
        animal = my_zoo.animals[0]
        if keeper:
            keeper.feed_animal(animal, "еда для животных")
        if vet:
            vet.heal_animal(animal)


    my_zoo.save_to_file(FILENAME)