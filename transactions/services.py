from django.db.models import Sum

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
    
    def calculate_account_balance(account):
        """ Calculate the current balance of an account."""
        income = ( Transaction.objects.filter(
            account = account,
            transaction_type ="income",
            is_active =True,
            ).aggregate(total=Sum("amount"))["total"] or 0
        )

        expense = (
            Transaction.objects.filter(
                account=account,
                transaction_type="expense",
                is_active=True,
            ).aggregate(total=Sum("amount"))["total"] or 0
        )

        return account.opening_balance + income - expense

    @staticmethod
    def get_account_summary(account):
        return {
            "opening_balance": account.opening_balance,
            "current_balance": TransactionService.calculate_account_balance(account),
        }
