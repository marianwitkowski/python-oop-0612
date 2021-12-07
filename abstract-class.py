"""
Klasa abstrakcyjna
"""

from abc import ABC, abstractmethod

class Figure(ABC):

    @abstractmethod # dekorator - poniższa metoda będzie uszczegółowiona w klasie potomnej
    def calc_area(self):
        pass

class Circle(Figure):
    """Klasa dziedzicząca po Figure"""
    def __init__(self, r):
        self.r = r

    def calc_area(self):
         return 3.14159*self.r**2

# figure = Figure()
# print(figure)
circle = Circle(2)
print(circle.calc_area())