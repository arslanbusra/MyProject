from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from attendance.models import Attendance
from leave.models import Leave
from datetime import date
from django.db.models import Sum


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            if user.user_type == 'employee':
                return redirect('employee_dashboard')
            elif user.user_type == 'manager':
                return redirect('manager_dashboard')
        else:
            return render(request, 'accounts/login.html', {'error': 'Invalid credentials'})
    return render(request, 'accounts/login.html')


def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def employee_dashboard(request):
    # Bugünkü giriş/çıkış bilgilerini al
    attendance = Attendance.objects.filter(user=request.user, date=date.today()).first()

    # Kullanıcının izin taleplerini al
    leave_requests = Leave.objects.filter(user=request.user)

    # Verileri şablona aktar
    return render(request, 'accounts/employee.html', {
        'attendance': attendance,
        'leave_requests': leave_requests,
    })


@login_required
def manager_dashboard(request):
    if request.user.user_type != 'manager':
        return redirect('employee_dashboard')  # Eğer kullanıcı manager değilse yönlendir

    # Giriş/çıkış saatleri
    attendances = Attendance.objects.all()

    # İzin talepleri
    leave_requests = Leave.objects.all()

    return render(request, 'accounts/manager.html', {
        'attendances': attendances,
        'leave_requests': leave_requests
    })

@login_required
def approve_leave(request, leave_id):
    leave = Leave.objects.get(id=leave_id)
    leave.status = 'approved'
    leave.save()
    return redirect('manager_dashboard')

@login_required
def reject_leave(request, leave_id):
    leave = Leave.objects.get(id=leave_id)
    leave.status = 'rejected'
    leave.save()
    return redirect('manager_dashboard')

@login_required
def monthly_report(request):
    month = request.GET.get('month')
    if not month:
        return redirect('manager_dashboard')

    year, month = map(int, month.split('-'))
    attendances = Attendance.objects.filter(
        date__year=year, date__month=month
    ).values('user__username').annotate(
        total_hours=Sum('total_work_hours')
    )

    return render(request, 'accounts/monthly_report.html', {'attendances': attendances})

