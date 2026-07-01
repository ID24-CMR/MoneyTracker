from rest_framework import serializers
from .models import SavingsGoals

class SavingSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavingsGoals
        fields = "__all__"
        read_only_fields = (
            "id",
            "user",
            "created_at",
        )