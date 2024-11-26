"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from accounts.views import login_view

urlpatterns = [
    # Admin paneli
    path('admin/', admin.site.urls),

    # Login sayfası
    path('', login_view, name='login'),

    # Accounts uygulaması URL'leri
    path('accounts/', include('accounts.urls')),

    # Attendance uygulaması URL'leri
    path('attendance/', include('attendance.urls')),

    # Leave uygulaması URL'leri
    path('leave/', include('leave.urls')),
]

