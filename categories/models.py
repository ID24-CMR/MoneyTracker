from django.db import models
from django.conf import settings

# Create your models here.
class Category(models.Model):
    CATEGORY_TYPES= [
        ("income", "INCOME"),
        ("expense", "EXPENSE"),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="categories"
    )

    name = models.CharField(max_length=100)

    category_type = models.CharField(
        max_length=20,
        choices=CATEGORY_TYPES
    )

    icon = models.CharField(
        max_length=50,
        default="folder",
    )

    color = models.CharField(
        max_length=20,
        default="#4CAF50"
    )

    is_default = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["name"]
        unique_together = ("user", "name")

    def __str__(self):
        return self.name