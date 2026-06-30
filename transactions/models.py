from django.db import models
from django.conf import settings
# Create your models here.
class Transaction(models.Model):
    TRANSACTION_TYPES = [
        ("income", "INCOME"),
        ("expense", "EXPENSE"),
        ("transfer", "TRANSFER"),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete= models.CASCADE,
        related_name="transactions"
    )

    account = models.ForeignKey(
        "accounts.Account",
        on_delete=models.CASCADE,
        related_name="transactions"
    )

    category = models.ForeignKey(
        "categories.Category",
        on_delete = models.SET_NULL,
        null=True,
        blank=True
    )

    transaction_type = models.CharField(
        max_length=20,
        choices=TRANSACTION_TYPES
    )

    amount = models.DecimalField(
        max_digits =15,
        decimal_places=2
    )

    transaction_date = models.DateField()
    reference = models-models.Field(max_field=100, blank=True)

    notes = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-transaction_date", "-created_at"]

    def __str__(self):
        return f"{self.transaction_type} - {self.amount}"