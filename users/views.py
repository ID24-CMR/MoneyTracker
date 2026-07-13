from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import RegisterForm
from categories.services import create_default_categories

# Create your views here.
def home(request):
    return render(request, "home.html")

# login views
def login_view(request):

    if request.user.is_authenticated:
        return redirect("dashboard")

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect("dashboard")
        else:
            messages.error(request, "Invalid username or password.")

    return render(request, "auth/login.html")

# dashboard views
@login_required
def dashboard(request):
    return render(request, "dashboard/dashboard.html")

# logout views
def logout_view(request):
    logout(request)
    return redirect("login")

# register views

def register_view(request):
    if request.user.is_authenticated:
        return redirect("dashboard")
    form = RegisterForm()

    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():

            user = form.save(commit=False)
            
            user.set_password(form.cleaned_data["password"]) #password is hashes before being save
            user.save()
            create_default_categories(user)
            messages.success(
                request,
                "Account created successfully. You can now log in."
            )
            return redirect("login")
    return render(
        request,
        "auth/register.html",
        {"form": form}
    )