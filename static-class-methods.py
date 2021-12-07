"""
 Metody statyczne i klasowe
"""
import random, time, os, sys

class User:
    """Klas z loginem i hasłem usera"""
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __str__(self):
        return f"{self.username}:{self.password}"

    @staticmethod # metoda statyczna
    def generate_password():
        random.seed(time.time_ns())
        return \
            "".join( random.choices("12345lmnopqrstuvw", k=8) )

    @classmethod # metoda klasowa
    def create_user(cls, username):
        return cls(username, User.generate_password())


class Utils:

    @staticmethod
    def only_even(items : list): # tylko parzyste
        return [item for item in items if item%2==0]

    def dummy_method(self):
        print("dummy....")

user = User("jnowak", User.generate_password())
print(user)

#time.sleep(4)
new_user = User.create_user("user1")
print(new_user)

print(Utils.only_even([1,3,4,7,8]))
print(Utils.only_even([1,3,4,7,8]))
Utils().dummy_method()