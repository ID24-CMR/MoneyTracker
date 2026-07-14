from django.contrib import admin
from .models import Transaction

# Register your models here.

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = (
        "reference",
        "user",
        "account",
        "category",
        "transaction_type",
        "amount",
        "transaction_date",
        "is_active",
    )

    search_fields = (
        "reference",
        "description",
    )
    list_filter = (
        "transaction_type",
        "transaction_date",
        "is_active",
    )