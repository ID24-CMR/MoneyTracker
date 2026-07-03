from django.db.models import Sum
from .models import Transaction

def get_transactions(user):
    return Transaction.objects.filter(user=user)

def get_total_income(user):
    return (
        Transaction.objects.filter(
            user=user,
            transaction_type="income"
        ).aggregate(total=Sum("amount"))["total"] or 0
    )

def get_total_expense(user):
    return (
        Transaction.objects.filter(
            user=user,
            transaction_type="expense"
        ).aggregate(total=Sum("amount"))["total"] or 0
    )

def get_recent_transactions(user, limit=10):
    return
    Transaction.objects.filter(user=user).order_by("-transaction_date")[:limit]