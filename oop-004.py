"""
Dziedziczenie w Pythonie
"""

class Animal:
    """Klasa ogólnie opisująca zwierzę"""
    def __init__(self, name, legs = 0):
        self._name = name.upper()
        self._legs = legs

    def __str__(self):
        return f"Zwierzę: {self._name}, nóg: {self._legs}"

class Bird(Animal):

    def __str__(self):
        return f"Ptak: {self._name}, nóg: {self._legs}"

    def fly(self):
        print(f"Odlatuje ptak: {self._name}")

    def run(self):
        return 1, f"Ptak {self._name} biega"

class Emu(Bird):

    def __init__(self, name, legs = 0, continent = "AFRICA"):
        super(Emu, self).__init__(name, legs)
        self._continent = continent

    def fly(self):
        print(f"Ptak {self._name} nie umie latać")

    def run(self):
        _, parent_response = super(Emu, self).run()
        return f"{parent_response}. I to bardzo szybko....".upper()

    def __str__(self):
        return f"Ptak: {self._name}, nóg: {self._legs}, {self._continent}"

#####
animal1 = Animal("pies", 4)
print(animal1)
print("="*60)

animal2 = Bird("Kura", 2)
print(animal2)
print(animal2.run())
print("="*60)

animal3 = Emu("Struś Pędziwiatr", 2, "AFRICA")
print(animal3)
animal3.fly()
print(animal3.run())
print("="*60)
