from django.db import models
from django.conf import settings

# Create your models here.
class Account(models.Model):
    ACCOUNT_TYPES = [
        ("cash", "Cash"),
        ("bank", "Bank Account"),
        ("mobile", "Mobile Money"),
        ("credit", "Credit Card"),
        ("savings", "Savings")
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete = models.CASCADE, related_name="accounts"
    )

    name = models.CharField(max_length=100)
    account_type = models.CharField(
        max_length=20,
        choices=ACCOUNT_TYPES
    )

    currency = models.CharField(
        max_length=10,
        default="CAD"
    )

    opening_balance = models.DecimalField(
        max_digits=15,
        decimal_places=2,
        default=0
    )

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        ordering = ["name"]
    
    def __str__(self):
        return self.name