from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import TransactionForm
from .models import Transaction

# Create your views here.
@login_required
def transaction_list(request):
    transactions = Transaction.objects.filter(
        user=request.user,
        is_active=True,
    )

    return render(
        request,
        "transactions/transaction_list.html",
        {
            "transactions": transactions,
        },
    )

@login_required
def transaction_create(request):
    if request.method == "POST":
        form = TransactionForm(request.POST, user=request.user)

        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.user =request.user
            transaction.save()

            messages.success(
                request,
                "Transaction created successfully."
            )
            return redirect("transaction_list")
    else:
        form = TransactionForm(user=request.user)
    return render(
        request,
        "transactions/transaction_create.html",
        {
            "form": form,
        },
    )