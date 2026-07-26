from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import BudgetForm
from .models import Budget


# Create your views here.
@login_required
def budget_list(request):

    budgets_list = Budget.objects.filter(user=request.user)
    return render(
        request,
        "budgets/budget_list.html",
        {
            "budgets": budgets_list
        })

@login_required
def budget_create(request):
    if request.method == "POST":
        form = BudgetForm(request.POST)

        if form.is_valid():
            budget = form.save(commit=False)
            budget.user = request.user
            budget.save()
            return redirect("budget_list")
    else:
        form = BudgetForm()

    return render(
        request,
        "budgets/budget_create.html",
        {
            "form": form
        })
