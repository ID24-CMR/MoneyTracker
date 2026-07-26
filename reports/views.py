from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from reports.services import get_monthly_report

# Create your views here.

@login_required
def report_dashboard(request):
    
    report = get_monthly_report(request.user)  # Assuming this function is defined elsewhere to fetch the report data
    return render(
        request,
        'reports/report_dashboard.html',
        {'report': report}
        )