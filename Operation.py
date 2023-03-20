import rsa
from Stage_2 import Signature
from Stage_3 import Account

class Operation:
    def __init__(self):
        self.sender = Account.Account()
        self.receiver = Account.Account()
        self.amount = int
        self.signature = bytes

    def create_operation(self, sender, receiver, amount, signature):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
        self.signature = signature
        return self

    def verify_operation(self, signature, amount):
        try:
            if self.sender.get_balance() >= amount:
                if Signature.Signature.verify_signature(signature, str(amount), self.sender.public_key) is True:
                    return True
                else:
                    return False
            else:
                return False
        except Exception as e:
            print(e)
            return False

    def to_string(self):
        operation_string = 'sender = ' + str(self.sender.to_string()) + ' receiver = ' + str(self.receiver.to_string()) + ' amount = ' + str(self.amount) + ' signature = ' + str(self.signature)
        return operation_string

    def print(self):
        print('Sender ', self.sender.to_string())
        print('Receiver ', self.receiver.to_string())
        print('Amount ', self.amount)
        print('Signature ', self.signature)
