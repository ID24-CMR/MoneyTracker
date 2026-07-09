from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from django.contrib import messages
from django.shortcuts import redirect

from .models import Account
from .forms import AccountForm

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

@login_required
def account_create(request):
    if request.method == "POST":
        form = AccountForm(request.POST)
        if form.is_valid():
            account = form.save(commit=False)
            account.user = request.user
            account.save()

            messages.success(request, "Account created successfully.")
            return redirect("account_list")
    else:
        form = AccountForm()
    
    return render(
        request,
        "accounts/account_create.html",
        {
            "form": form
        }
    )