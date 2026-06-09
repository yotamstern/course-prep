


class Animal:
    zoo_name = "Hayaton"
    def __init__(self, name, hunger=0):
        self._name = name
        self._hunger = hunger

    def get_name(self):
        return self._name

    def is_hungry(self) -> bool:
        return self._hunger > 0

    def feed(self):
        self._hunger -= 1

    def talk(self):
        pass


class Dog(Animal):
    def talk(self):
        print("woof woof")

class Cat(Animal):
    def talk(self):
        print("meow")

class Skunk(Animal):
    def __init__(self, name, hunger=0, stink_count=6):
        super().__init__(name,hunger)
        self._stink_count = stink_count


    def talk(self):
        print("tssssss")

class Unicorn(Animal):
    def talk(self):
        print("Good day, darling")

class Dragon(Animal):
    def __init__(self, name, hunger, color="Green"):
        super().__init__(name, hunger)
        self._color = color

    def talk(self):
        print("Raaawr")



def main():
    animal_list = [Dog("Brownie", 10), Cat("Zelda", 3), Skunk("Stinky", 0, 5),Unicorn("Keith", 7), Dragon("Lizzy", 1450,"Blue"), Dog("Doggo",80),Cat("Kitty", 80),Skunk("Stinky Jr.", 80, 5), Unicorn("Clair", 80),Dragon("McFly", 80, "Green")]
    for animal in animal_list:
        has_run = False
        while animal.is_hungry():
            if not has_run:
                print(f"Type of animal: {type(animal).__name__} \nName: {animal.get_name()}")
                has_run = True
            animal.feed()
            animal.talk()
    print(Animal.zoo_name)


if __name__ == '__main__':
    main()

