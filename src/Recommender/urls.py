"""Recommender URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from src.Home.views import home_view, register_view, base_view, logged_in_view, Import_view, Import_Breweryview,AccountSettings_view
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('home/', home_view, name='home'),
    path('logged_in/', logged_in_view, name='logged_in'),
    path('base/', base_view, name='base'),    
    path('admin/', admin.site.urls),
    path('register/', register_view, name='register'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('Import/', Import_view, name='import'),
    path('ImportBrewery/', Import_Breweryview, name='importbrewery'),
    path('AccountSettings/', AccountSettings_view, name='AccountSettings'),

    
]
