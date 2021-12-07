"""
 Realizacja scenariusza zakupowego
"""
from product import Product
from orderitem import OrderItem
from basket import Basket

product1 = Product(1, "Pendrive", 49.99)
product2 = Product(2, "Mysz Logitech", 119.99)
product3 = Product(3, "Słuchawki JBL", 299)

basket = Basket()
basket.add(product1, 3)
basket.add(product2, 1)
basket.add(product3, 1)
basket.add(product1, 5)
basket.remove(product2)
basket.show()
basket.get_total_amount()
basket.clear()



