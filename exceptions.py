from account_class import Account

class Error(Exception):
    pass

class InsufficientFundsError(Exception):
    """Raised when the balance is less than zero"""
    pass

while True:
    try:
        if self._withdraw > self._balance:
            raise InsufficientFundsError
        break
    except InsufficientFundsError:
        print("Insufficient Funds")