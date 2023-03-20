import rsa
from Stage_2 import Signature
from Stage_3 import Account
from Stage_4 import Operation

class Transaction:
    def __init__(self):
        self.initiator = Account.Account().account_id
        self.operations = [Operation.Operation()]
        self.nonce = int

    def create_transaction(self, initiator, operations):
        self.initiator = initiator
        self.operations = operations
        self.nonce = hash(tuple(operations)) + hash(initiator)
        return self

    def to_string(self):
        transaction_string = 'initiator = ' + self.initiator.to_string() + ' operations = ' + ''.join(operation.to_string() for operation in self.operations) + ' nonce = ' + str(self.nonce)
        return transaction_string

    def print(self):
        print('Initiator ', self.initiator.to_string())
        print('Operations ', ''.join(operation.to_string() for operation in self.operations))
        print('Nonce ', self.nonce)
