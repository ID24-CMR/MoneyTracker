from accounts.models import Account
from django.db.models import Sum
from django.utils import timezone
from transactions.models import Transaction
from transactions.services import TransactionService


def get_dashboard_summary(user):
    """ Calculate the dashboard summary for a user."""
    
    accounts = Account.objects.filter(
        user = user,
        is_active=True,
    )

    total_balance = 0
    
    for account in accounts:
        total_balance += TransactionService.calculate_account_balance(account)
    
    monthly_summary = get_monthly_summary(user)
    recent_transactions = get_recent_transactions(user)
    expenses_by_category = get_expenses_by_category(user)

    print("recent_transactions:", recent_transactions)  # Debugging line to print recent transactions

    return {
        "total_balance": total_balance,
        "accounts": accounts,
        "total_income": monthly_summary["monthly_income"],
        "total_expenses": monthly_summary["monthly_expenses"],
        "recent_transactions": recent_transactions,
        "expenses_by_category": expenses_by_category,
    }

def get_monthly_summary(user):

    total = timezone.now()

    income = (
        Transaction.objects.filter(
            user=user,
            transaction_type="income",
            is_active=True,
            transaction_date__year=total.year,
            transaction_date__month=total.month,
        ).aggregate(total=Sum("amount"))["total"] or 0
    )

    expenses = (
        Transaction.objects.filter(
            user=user,
            transaction_type="expense",
            is_active=True,
            transaction_date__year=total.year,
            transaction_date__month=total.month,
        ).aggregate(total=Sum("amount"))["total"] or 0
    )

    return {
        "monthly_income": income,
        "monthly_expenses": expenses,
    }

def get_recent_transactions(user, limit=5):
    """ Fetch the most recent transactions for a user."""
    return Transaction.objects.filter(
        user=user,
        is_active=True,
    ).select_related(
        "account",
        "category",
    ).order_by(
        "-transaction_date",
        "-created_at",
    )[ : limit ]


def get_expenses_by_category(user):

    return list(
        Transaction.objects.filter(
            user=user,
            transaction_type="expense",
            is_active=True,
        ).values("category__name").annotate(total=Sum("amount")).order_by("-total")
    )
