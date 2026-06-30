from django.db import models

# Create your models here.
from django.conf import settings

class Budget(models.Model):
    PERIODS = [
        ("weekly", "Weekly"),
        ("monthly", "Monthly"),
        ("yearly", "Yearly"),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="budgets"
    )

    category = models.ForeignKey(
        "categories.Category",
        on_delete=models.CASCADE
    )

    period = models.CharField(
        max_length=20,
        choices=PERIODS,
        default="monthly"
    )

    amount_date = models.DateField(
        max_digits=15,
        decimal_places=2
    )

    start_date = models.DateField()

    end_date = models.DateField()

    created_at = models.DateTimeField(auto_now_add=True)