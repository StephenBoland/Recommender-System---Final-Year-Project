from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from src.Home.forms import RegistrationForm


def home_view(request, *args, **kwargs):
    return render(request, "home.html", {})
def base_view(request, *args, **kwargs):
    return render(request,"base.html", {})

def register_view(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid(): #is the form valid? filled out properly
            user = form.save() #save the users detail
            login(request, user)
            return redirect("/home")
        else:
            for msg in form.error_messages:
                print(form.error_messages[msg])
            
    
    form = RegistrationForm()
    return render(request,
                  "register.html",
                  context={"form":form})
