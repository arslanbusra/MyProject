from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    user_type_choices=(
        ('employee','employee'), #kişi employee seçerse kullanıcı employee için açılır
        ('manager','manager'), #kişi manager seçerse manager için ekran açılır
    )

    user_type=models.CharField(max_length=10, choices=user_type_choices, default='employee')

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_groups',  # Çakışmayı önlemek için yeni ilişki adı
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions',  # Çakışmayı önlemek için yeni ilişki adı
        blank=True
    )
    
    
    def __str__(self):
        return f" ${self.username} - {self.user_type}"


