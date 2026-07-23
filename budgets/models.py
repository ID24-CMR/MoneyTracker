# Create your models here.
from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()
class Budget(models.Model):
    
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="budgets"
    )

    category = models.ForeignKey(
        "categories.Category",
        on_delete=models.CASCADE
    )

    amount_limit = models.DecimalField(
        max_digits=15,
        decimal_places=2
    )

    month = models.PositiveSmallIntegerField(default=True)

    year = models.PositiveSmallIntegerField(default=True)

    is_active = models.BooleanField(default=True)

    start_date = models.DateField()

    end_date = models.DateField()

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "category", "month", "year")

    def __str__(self):
        return f"{self.user.username} - {self.category.name} - {self.month}/{self.year}"
