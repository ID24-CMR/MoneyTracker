from .models import Transaction
from .validators import TransactionValidator

class TransactionService:
    def create_transaction(**date):
        transaction = Transaction(**date)
        TransactionValidator.validate_transaction(transaction)

        transaction.save()
        return transaction
    @staticmethod
    def delete_transaction(transaction):
        transaction.delete()