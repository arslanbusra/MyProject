from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('employee/', views.employee_dashboard, name='employee_dashboard'),
    path('manager/', views.manager_dashboard, name='manager_dashboard'),
    path('manager/approve-leave/<int:leave_id>/', views.approve_leave, name='approve_leave'),
    path('manager/reject-leave/<int:leave_id>/', views.reject_leave, name='reject_leave'),
    path('manager/monthly-report/', views.monthly_report, name='monthly_report'),

]
