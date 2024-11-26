from django.contrib import admin
from .models import User  # User modelinizi import edin

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'user_type', 'is_active', 'is_staff')  # Görüntüleme alanları
    search_fields = ('username', 'email')  # Arama yapılabilecek alanlar
    list_filter = ('user_type', 'is_active', 'is_staff')  # Filtreleme seçenekleri

