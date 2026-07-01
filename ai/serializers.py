from rest_framework import serializers
from .models import AI
class AISerializer(serializers.ModelSerializer):
    class Meta:
        model = AI
        fields = "__all__"
        read_only_fields = (
            "id",
            "user",
            "generated_at",
        )