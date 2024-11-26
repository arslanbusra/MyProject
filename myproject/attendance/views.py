from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Attendance
from datetime import date, datetime

@login_required
def mark_attendance(request):
    if request.method == 'POST':
        entry_time = request.POST.get('entry_time')
        exit_time = request.POST.get('exit_time')

        if entry_time:
            entry_time = datetime.strptime(entry_time, '%H:%M').time()
        if exit_time:
            exit_time = datetime.strptime(exit_time, '%H:%M').time()

        # Bugün için kaydı al veya oluştur
        attendance, created = Attendance.objects.get_or_create(
            user=request.user,
            date=date.today()
        )
        attendance.first_entry = entry_time
        attendance.last_exit = exit_time
        attendance.save()

        return redirect('employee_dashboard')

    # Bugünün katılım bilgilerini şablona gönder
    attendance = Attendance.objects.filter(user=request.user, date=date.today()).first()
    return render(request, 'attendance/mark_attendance.html', {'attendance': attendance})




