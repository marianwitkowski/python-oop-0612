from product import Product
from orderitem import OrderItem

class Basket:
    """Klasa opisująca koszyk zamówień/listę pozycji zamówienia"""
    def __init__(self):
        self.items = [] # pusta lista pozycji zamówienia

    def clear(self):
        """Czyści koszyk"""
        self.items.clear()

    def get_total_amount(self):
        """Ile do zapłaty"""
        pass

    def add(self, product : Product, qnty):
        """Dodaje elementy do pozycji zamówienia (lub akualizuje pozycję)"""
        if qnty<=0: raise ValueError("Niepoprawna liczba produktów")
        for item in self.items:
            if item.product.id == product.id:
                item.qnty += qnty # item.qnty = item.qnty + qnty
                return
        new_item = OrderItem(product, qnty)
        self.items.append(new_item)

    # def remove(self, product):
    #     """Kompletnie usuwa pozycję zamówienia dotycząca produktu z parametru product"""
    #     for index, item in enumerate(self.items):
    #         if item.product.id == product.id:
    #             #self.items.remove(item)
    #             self.items.pop(index)
    #             return

    def remove(self, product):
        """Kompletnie usuwa pozycję zamówienia dotycząca produktu z parametru product"""
        res = list(filter(lambda item: item.product.id == product.id, self.items))
        if len(res)==1:
            self.items.remove(res[0])

    def show(self):
        print("="*40)
        for item in self.items:
            print(f"{item.product.id} - {item.product.name} - {item.qnty}")
