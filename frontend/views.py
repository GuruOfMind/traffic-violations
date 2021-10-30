from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
import requests
from requests.models import Response
from rest_framework import status

def Home_view(request, *args, **kwargs):
    print(request.user)
    return render(request, "home.html", {})

def Login_view(request, *args, **kwargs):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
        
            return redirect("home")
        else:
            return redirect("home")
    return render(request, "login.html", {})

def Logout_view(request, *args, **kwargs):
    logout(request)
    return redirect('home')

def Regsiter_view(request, *args, **kwargs):
    if request.method == "POST":
        payload = {"plugged_number": request.POST.get("plugged_number"), "driver": request.POST.get("driver"), "category": request.POST.get("category"), "type": request.POST.get("type"), "production_date": request.POST.get("production_date"), "registration_date": request.POST.get("registration_date")}
        response = requests.post("http://127.0.0.1:8000/api/vehicles/", data=payload)
        if response.status_code == 201:
            data = response.json()
            return redirect("login")
        else:
            print(response.content)
            return redirect("home")
    else:
        return render(request, "register.html", {})
    return render(request, "register.html", {})
        
@login_required(login_url="/login")
def Dashboard_view(request, *args, **kwargs):
    response = requests.get("http://127.0.0.1:8000/api/vehicle-violation-logs/")
    violations_list = response.json()
    return render(request, "dashboard.html", {"violations_list": violations_list})

def Detail_view(request, id, *args, **kwargs):
    url = f"http://127.0.0.1:8000/api/vehicle-violation-logs/{id}"
    response = requests.get(url)
    violation_details = response.json()
    return render(request, "violation.html", {"violation_details": violation_details})