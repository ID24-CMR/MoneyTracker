from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import TransactionForm
from .models import Transaction

# Create your views here.
@login_required
def transaction_list(request):
    transactions = Transaction.objects.filter(
        user=request.user, #this ensures that users can only see or access their own transaction
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
            transaction.transaction_type = transaction.category.category_type
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

@login_required
def transaction_detail(request, pk):
    transaction = get_object_or_404(
        Transaction,
        pk=pk,
        user=request.user,
        is_active=True,
    )

    return render(
        request,
        "transactions/transaction_detail.html",
        {
            "transaction": transaction,
        },
    )

@login_required
def transaction_update(request, pk):
    transaction = get_object_or_404(
        Transaction,
        pk=pk,
        user=request.user,
        is_active=True,
    )

    if request.method == 'POST':
        form = TransactionForm(
            request.POST,
            instance=transaction,
            user=request.user,
        )

        if form.is_valid():
            form.save()
            messages.success(
                request,
                "Transaction updated successfully."
            )
            return redirect("transaction_list")
    else:
        form = TransactionForm(
            instance=transaction,
            user=request.user,
        )
    return render(
        request,
        "transactions/transaction_update.html",
        {
            "form": form,
            "transaction": transaction,
        },
    )

@login_required
def transaction_archive(request, pk):
    transaction = get_object_or_404(
        Transaction,
        pk=pk,
        user=request.user,
        is_active=True,
    )

    if request.method == 'POST':
        transaction.is_active = False
        transaction.save()

        messages.success(
            request,
            "Transaction archived successfully."
        )

        return redirect("transaction_list")
    return render(
        request,
        "transactions/transaction_archive.html",
        {
            "transaction": transaction,
        },
    )