# class Error(Exception):
#     pass
#
# class InsufficientFundsError(Exception):
#     """Raised when the balance is less than zero"""
#     pass
#
# while True:
#     try:
#         if self._withdraw > self._balance:
#             raise InsufficientFundsError
#         break
#     except InsufficientFundsError:
#         print("Insufficient Funds")


class Account:

    def __init__(self, firstname, surname, age, balance=0):
        self._firstname = firstname
        self._surname = surname
        self._age = age
        self._balance = balance


    def deposit(self, amount):
        try:
            self._balance += amount
        except TypeError as err:
            print("Value of deposit cannot be a string")

    def withdraw(self, amount):
        self._balance -= amount

    def getbalance(self):
        return self._balance









