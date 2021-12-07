"""
 Pola prywatne, publiczne i chronione w Pythonie
"""

class BankAccount:

    def __init__(self, name, address, total):
        self.name = name # pola publiczne
        self._address = address # pola chronione
        self.__total = total # pola "prywatne"

    def __str__(self):
        return f"konto: {self.name}, total: {self.__total}"

account = BankAccount("Jan Kowalski", "Zielona 12", 12345)
print(account)
account.__total = 0
account._BankAccount__total = 0
print(account)

