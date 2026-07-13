from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required


from .models import Category
from .forms import CategoryForm
# Create your views here.
@login_required
def category_list(request):

    categories = Category.objects.filter(
        user=request.user,
        is_active=True,
    ).order_by("category_type", "name")

    return render(
        request,
        "categories/category_list.html",
        {
            "categories": categories
        }
    )

@login_required
def category_create(request):

    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.user = request.user
            category.save()

            messages.success(
                request,
                "category created successfully."
            )
            return redirect("category_list")
    else:
        form = CategoryForm()
    return render(
        request,
        "categories/category_create.html",
        {
            "form":form
        }
    )

@login_required
def category_update(request, pk):
    category = get_object_or_404(
        Category,
        pk=pk,
        user=request.user,
        is_active=True
    )

    if request.method == "POST":
        form = CategoryForm(request.POST, instance=category)

        if form.is_valid():
            form.save()

            messages.success(
                    request,
                    "Category updated successfully!"
                )
            return redirect("category_list")
    else:
        form = CategoryForm(
            instance=category
        )
    return render(
        request,
        "categories/category_update.html",
        {
            "form": form,
            "category": category,
        }
    )