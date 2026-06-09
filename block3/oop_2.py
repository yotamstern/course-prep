
class Octopus:
    octo_counter = 0
    def __init__(self, name="Octavio", age=0):
        self._name = name
        self._age = age
        Octopus.octo_counter += 1

    def birthday(self):
        self._age += 1

    @property
    def age(self) -> int:
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name):
        self._name = name





def main():
    oct_1 = Octopus("Octavion", 1)
    oct_2 = Octopus("Octavious", 2)
    print(f"Age of {oct_1.name} is: {oct_1.age}")
    print(f"Age of {oct_2.name} is: {oct_2.age}")

    oct_1.birthday()
    print(f"\nToday's {oct_1.name}'s birthday!!")
    print(f"Age of {oct_1.name} is: {oct_1.age}")
    print(f"Total amount of octopus created: {Octopus.octo_counter}")



if __name__ == "__main__":
    main()


