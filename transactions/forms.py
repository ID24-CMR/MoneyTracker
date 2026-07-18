from accounts.models import Account
from categories.models import Category
from django import forms

from .models import Transaction


class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = [
            "account",
            "category",
            "amount",
            "transaction_date",
            "description",
            "notes",
        ]

        widgets = {
            "transaction_date": forms.DateInput(
                attrs={"type": "date"}
            ),
            "notes": forms.Textarea(
                attrs={"rows": 4}
            ),
        }
    
    def __init__(self, *args, user=None, **kwargs):
        super().__init__(*args, **kwargs)

        if user:
            self.fields["account"].queryset = Account.objects.filter(
                user=user,
                is_active=True
            )
            self.fields["category"].queryset = Category.objects.filter(
                user=user,
                is_active=True
            )
