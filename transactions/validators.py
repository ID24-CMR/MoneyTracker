

from decimal import Decimal
from django.core.exceptions import ValidationError


class TransactionValidator:
    @staticmethod
    def validate_amount(amount):
        if amount <= Decimal("0"):
            raise ValidationError("Amount must be greater than zero.")
    
    @staticmethod
    def validate_account(account):
        if not account.is_active:
            raise ValidationError("This account is inactive.")
    
    @staticmethod
    def validate_transaction(transaction):
        TransactionValidator.validate_amount(transaction.amount)
        TransactionValidator.validate_account(transaction.account)