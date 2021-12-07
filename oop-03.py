"""
Przeciązanie operatorów
"""
class Vector:
    """Klasa opisująca wektor"""
    def __init__(self,x, y):
        self.x = x; self.y = y

    def __str__(self):
        return f"Wektor [{self.x},{self.y}]"

    def add_vector(self, other_vector):
        return Vector(self.x + other_vector.x, self.y + other_vector.y)

    def __add__(self, other_object):
        if type(other_object) is Vector:
            return self.add_vector(other_object)
        elif type(other_object) in [int, float]:
            return Vector(self.x+other_object, self.y+other_object)
        elif type(other_object) in [tuple, list]:
            #other_object = other_object[:2]
            if len(other_object)==0: raise ValueError("Zła ilość danych")
            if len(other_object)==1:
                return Vector(self.x+other_object[0], self.y+other_object[0])
            return Vector(self.x+other_object[0], self.y+other_object[1])
        elif type(other_object) is dict:
            if "x" in other_object and "y" in other_object:
                return Vector(self.x+other_object["x"], self.y+other_object["y"])
            else:
                raise ValueError("Słownik musi mieć klucze x i y")
        else:
            return None

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other): # !=
        ...

    def __lt__(self, other): # <
        pass

    def __gt__(self, other): # >
        pass

    def __le__(self, other): # <=
        pass

    def __ge__(self, other): # >=
        pass

### obsługa klasy ###
vector1 = Vector(1, 2)
print(vector1)
vector2 = Vector(-3, 3)
print(vector2)

vector3 = vector1.add_vector(vector2)
print(vector3)

vector3 = vector1 + 5 #vector2
print(vector3)

vector3 = vector1 + [1]
print(vector3)

vector3 = vector1 + (1,2)
print(vector3)

vector3 = vector1 + { "x" : 1, "y": -1 }
print(vector3)

vector1 = Vector(1,-1)
vector2 = Vector(1,-1)
result = vector1 == vector2
print(result)



