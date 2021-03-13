from account_class import Account
from currentaccount_class import Current
from exceptions import Error
from exceptions import InsufficientFundsError

chiara = Account("Chiara", "Dinan", 23, 1000)


# amount_withdrawn = int(input("Please ent")
print(chiara.withdraw(2000))
print(chiara.getbalance())



