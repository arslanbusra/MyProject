from django.db import models
from accounts.models import User

class Leave(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    leave_type = models.CharField(max_length=20, choices=[('annual', 'Annual Leave'), ('sick', 'Sick Leave')])
    start_date = models.DateField(default='2024-01-01')
    end_date = models.DateField(default='2024-01-02')
    status = models.CharField(max_length=10, choices=[('pending', 'Pending'), ('approved', 'Approved')], default='pending')

    

    def __str__(self):
        return f"{self.user.username}-${self.total_leave}"
    

