from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Account

# Create your views here.
@login_required
def account_list(request):
    accounts = Account.objects.filter(
        user=request.user,
        is_active=True
    )

    context = {
        "accounts": accounts,
    }

    return render(
        request,
        "accounts/account_list.html", context
    )