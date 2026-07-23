from django.contrib import admin

from .models import Budget


# Register your models here.
@admin.register(Budget)
class BudgetAdmin(admin.ModelAdmin):
    list_display = ("user", "category", "amount_limit", "month", "year")
