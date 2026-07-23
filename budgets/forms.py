from django import forms

from .models import Budget


class BudgetForm(forms.ModelForm):

    class Meta:
        model = Budget
        fields = ["category", "amount_limit", "month", "year"]

        widgets = {
            "month": forms.NumberInput(attrs={"class": "form-control", "min": 1, "max": 12}),
            "year": forms.NumberInput(attrs={"class": "form-control", "min": 2000, "max": 2100}),
        }
