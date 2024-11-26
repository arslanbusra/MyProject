from django.db import models
from accounts.models import User

class Attendance(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE) #users models.py dosyasını import ederek user yapısı ile attendance kısmını ilişkilendirdik.
    date=models.DateField(auto_now=True)
    first_entry=models.TimeField(null=True,blank=True)
    last_exit=models.TimeField(null=True, blank=True)
    late_minutes=models.IntegerField(default=0)
    total_work_hours = models.DurationField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.first_entry and self.last_exit:
            from datetime import datetime
            start_time = datetime.combine(self.date, self.first_entry)
            end_time = datetime.combine(self.date, self.last_exit)
            self.total_work_hours = end_time - start_time
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.username} - {self.date}"