class Animal:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def make_sound(self):

        print(f"{self.name} издаёт звук.")

    def eat(self, food: str):
        """Общий метод кормления."""
        print(f"{self.name} ест {food}.")


class Bird(Animal):
    def __init__(self, name: str, age: int, wing_span: float):
        super().__init__(name, age)
        self.wing_span = wing_span  # размах крыльев в сантиметрах

    def make_sound(self):
        print(f"{self.name} чирикает: «Чиррик-чиррик!»")

    def fly(self):
        print(f"{self.name} летит с размахом крыльев {self.wing_span} см.")


class Mammal(Animal):
    def __init__(self, name: str, age: int, fur_color: str):
        super().__init__(name, age)
        self.fur_color = fur_color

    def make_sound(self):
        print(f"{self.name} издает млекопитающий звук: «Гррр!»")

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


def animal_sound(animals):


    for animal in animals:
        animal.make_sound()


if __name__ == "__main__":
    # Создаём несколько объектов разных подклассов
    tweety = Bird(name="Твити", age=1, wing_span=25.0)
    bella = Mammal(name="Белла", age=4, fur_color="коричневый")
    sly = Reptile(name="Слай", age=2, scale_type="гладкую")


    zoo = [tweety, bella, sly]
    animal_sound(zoo)


    tweety.fly()
    bella.eat("корм для собак")
    sly.shed_skin()