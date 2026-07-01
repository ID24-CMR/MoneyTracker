from django.db import models
from django.conf import settings
# Create your models here.

class AI(models.Model):

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="ai_insights"
    )

    title =  models.CharField(max_length=200)

    summary = models.TextField()

    recommendation = models.TextField()

    confidence = models.DecimalField(
        max_digits=4,
        decimal_places=2
    )

    generated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-generated_at"]