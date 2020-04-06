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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from src.Home.views import home_view, register_view, base_view, Import_view, Import_Breweryview,AccountFavourites_view, logged_in_view, logged_in_base_view, logout
from django.contrib.auth.views import LoginView
from Database.views import beer_detail_view, brew_detail_view, Homebeer_detail_view,stout_view,ale_view,porter_view,larger_view,NonAlcoholic_view,dynamic_lookup_viewBeer,\
    dynamic_lookup_viewBrewery,dynamic_lookup_viewLarger,dynamic_lookup_viewPorter,dynamic_lookup_viewAle,dynamic_lookup_viewStout,dynamic_lookup_viewNA,dynamic_lookup_viewHome
from django.conf.urls.static import static
from django.conf import settings
from Preferences.views import User_Preferences, RecommendedPageView, dynamic_lookup_viewRecommendedPage, edit_profile, change_password


urlpatterns = [

    path('home/', Homebeer_detail_view, name='home'),
    path('beerhome/', beer_detail_view, name='beerhome'),
    path('NonAlcoholic/', NonAlcoholic_view, name='nonalcoholic'),
    path('Largers/', larger_view, name='largers'),
    path('BeerView/<int:pk>/', dynamic_lookup_viewBeer, name='BeerView'),
    path('BrewView/<int:pk>/', dynamic_lookup_viewBrewery, name='BrewView'),
    path('BeerViewLarger/<int:pk>/', dynamic_lookup_viewLarger, name='BeerViewLarger'),
    path('BeerViewStout/<int:pk>/', dynamic_lookup_viewStout, name='BeerViewStout'),
    path('BeerViewAle/<int:pk>/', dynamic_lookup_viewAle, name='BeerViewAle'),
    path('BeerViewPorter/<int:pk>/', dynamic_lookup_viewPorter, name='BeerViewPorter'),
    path('BeerViewNA/<int:pk>/', dynamic_lookup_viewNA, name='BeerViewNA'),
    path('BeerViewRanked/<int:pk>/', dynamic_lookup_viewHome, name='BeerViewRanked'),
    path('RecommendedPage/<int:pk>/', dynamic_lookup_viewRecommendedPage, name='RecommendedPageView'),
    path('RecommendedPageView/', RecommendedPageView, name='RecommendedBeer'),
    path('Stouts/', stout_view, name='stouts'),
    path('Porters/', porter_view, name='porters'),
    path('Ales/', ale_view, name='ales'),
    path('brewhome/', brew_detail_view, name='brewhome'),
    path('logged_in/', logged_in_view, name='logged_in'),
    path('logout/', logout, name='logout'),
    path('base/', base_view, name='base'),
    path('logged_in_base/', logged_in_base_view, name='logged_in_base'),
    path('admin/', admin.site.urls),
    path('register/', register_view, name='register'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('Import/', Import_view, name='import'),
    path('ImportBrewery/', Import_Breweryview, name='importbrewery'),
    path('AccountPreferences/', User_Preferences, name='AccountPreferences'),
    path('AccountSettings/', edit_profile, name='AccountSettings'),
    path('password/', change_password, name='change_password'),

    # path('AccountSettings/', profile, name='AccountSettings'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

    

