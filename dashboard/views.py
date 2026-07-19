from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from dashboard.services import get_dashboard_summary

# Create your views here.

@login_required
def dashboard_view(request):
    """ Render the dashboard view for the logged-in user."""
    context = get_dashboard_summary(request.user)
    
    print("Dashboard Summary:", context)  # Debugging line to print the context

    return render(request, "dashboard/dashboard.html", {"dashboard_summary": context})
