from django import forms
from .models import Account

class AccountForm(forms.ModelForm):
    class Meta:
        model = Account

        fields = [
            "name",
            "account_type",
            "currency",
            "opening_balance",
        ]

        widgets = {
            "name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Account Name"
            }),

            "account_type": forms.Select(attrs={
                "class": "form-control"
            }),

            "currency": forms.Select(attrs={
                "class": "form-control"
            }),

            "opening_balance": forms.NumberInput(attrs={
                "class": "form-control",

                "step": "0.01"
            })
        }