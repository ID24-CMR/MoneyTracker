from django.db.models import Sum
from django.utils import timezone

from transactions.models import Transaction

def get_monthly_report(user):

    today = timezone.now().now()

    income = (
        Transaction.objects.filter(
            user=user,
            transaction_type='income',
            is_active=True,
            transaction_date__year=today.year,
            transaction_date__month=today.month,
        ).aggregate(total=Sum('amount'))['total'] or 0
    )

    expenses = (
        Transaction.objects.filter(
            user=user,
            transaction_type='expense',
            is_active=True,
            transaction_date__year=today.year,
            transaction_date__month=today.month,
        ).aggregate(total=Sum('amount'))['total'] or 0
    )

    return {
        'income': income,
        'expenses': expenses,
        'net_income': income - expenses,
    }