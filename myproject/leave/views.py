from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Leave

@login_required
def request_leave(request):
    if request.method == 'POST':
        leave_type = request.POST.get('leave_type')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        leave = Leave.objects.create(
            user=request.user,
            leave_type=leave_type,
            start_date=start_date,
            end_date=end_date,
            status='pending'
        )
        return redirect('employee_dashboard')
    return render(request, 'leave/request_leave.html')



