from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from transactions.services import TransactionService

from .forms import AccountForm
from .models import Account


# Create your views here.
@login_required
def account_list(request):
    accounts = Account.objects.filter(
        user=request.user,
        is_active=True
    )

    account_data = []
    for account in accounts:
        summary = TransactionService.get_account_summary(account)
        account_data.append({
            "account": account,
            "current_balance": summary["current_balance"],
        })

    return render(
        request,
        "accounts/account_list.html",
        {
            "account_data": account_data,
        },
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

@login_required
def account_update(request, pk):
    account = get_object_or_404(
        Account,
        pk=pk,
        user=request.user,
        is_active=True
    )
    if request.method == 'POST':
        form = AccountForm(
            request.POST,
            instance=account
        )
        if form.is_valid():
            form.save()
            messages.success(
                request,
                "account updated successfully."
            )
            return redirect("account_list")
    else:
        form = AccountForm(instance=account)
    return render(
        request,
        "accounts/account_update.html",
        {
            "form": form,
            "account": account,
        }
    )

@login_required
def account_detail(request, pk):
    account = get_object_or_404(
        Account,
        pk=pk,
        user=request.user,
        is_active=True,
    )
    context = {
        "account": account,
    }

    return render(
        request,
        "accounts/account_detail.html",
        context,
    )

@login_required
def account_archive(request, pk):
    account = get_object_or_404(
        Account,
        pk=pk,
        user=request.user,
        is_active=True,
    )
    if request.method== "POST":
        account.is_active = False
        account.save()

        messages.success(
            request,
            "Account archived successfully."
        )
        return redirect("account_list")
    return render(
        request,
        "accounts/account_archive.html",
        {
            "account": account
        }
    )
