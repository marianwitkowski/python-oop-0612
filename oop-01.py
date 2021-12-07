"""
 OOP - przykładowa klasa
"""
from datetime import datetime
from typing import Union, List, Optional, Tuple

class ExampleClass:
    pass


# ec1 = ExampleClass()
# print(id(ec1))
#
# ec2 = ExampleClass()
# print(id(ec2))

class Product:
    """Klasa opisująca produkt"""

    def __init__(self, id: int, name: str,
                 price: [float,int], input_date = None):
        if input_date is None:
            input_date = datetime.now()
        if not type(input_date) is datetime:
            raise TypeError("Parametr datetime nie jest datą")
        if not type(id) is int:
            raise TypeError("Parametr id nie jest int")
        if not type(name) is str:
            raise TypeError("Parametr name nie jest str")
        if not type(price) in [int, float]:
            raise TypeError("Parametr price nie jest float lub int")

        self.id = id; self.name = name
        self.price = price
        self.price_changes = []

    def __str__(self):
        return f"Produkt: {self.id}, {self.name}, " \
               f"{self.price} PLN"

    def update_price(self, new_price: float) -> bool:
        if new_price <= 0:
            return False
        self.price_changes.append(self.price)
        self.price = new_price
        return True

    def update_price_exc(self, new_price: float):
        if new_price <= 0:
            raise ValueError("Kwota mniejsza niż zero.")
        self.price_changes.append(self.price)
        self.price = new_price

    def update_price_tuple(self, new_price: float) -> tuple:
        if new_price <= 0:
            return -1, "Cena mniejsza zero."
        self.price_changes.append(self.price)
        self.price = new_price
        return 0,

    def update_productid(self, new_id:Union[int,str]):
        pass

    def dummyset(self, vars:List[int], extra:Tuple[int, ...]):
        pass

price_changes = []
product1 = Product(1, "Cukier", 3)
print(product1)
# aktualizacja ceny
# price_changes.append( (product1.price,datetime.now()) )
# product1.price = 3.99
product1.update_price(3.99)
print(product1)
product1.dummyset({"x":1}, ("A","B",12,34) )

try:
    product1.update_price_exc(-1)
except ValueError as exc:
    print(exc)
except Exception as exc:
    print(exc)

product1.update_price_tuple(4.99)