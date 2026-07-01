from django.db import models
from django.conf import settings

# Create your models here.

class SavingsGoals(models.Model):

    STATUS = [
        ("active", "Active"),
        ("completed", "Completed"),
        ("cancelled", "Cancelled"),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="saving_gaols"
    )

    title = models.CharField(max_length=200)

    description = models.TextField(blank=True)

    target_amount = models.DecimalField(
        max_digits=15,
        decimal_places=2
    )

    current_amount = models.DecimalField(
        max_digits=15,
        decimal_places=2,
        default=0
    )

    deadline = models.DateField()

    status = models.CharField(
        max_length=20,
        choices=STATUS,
        default="active"
    )

    created_at = models.DateTimeField(auto_now_add=True)