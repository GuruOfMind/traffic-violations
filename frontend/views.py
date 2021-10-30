from django.contrib.auth.decorators import login_required
from django.shortcuts import render
import requests

def Home_view(request, *args, **kwargs):
    print(request.user)
    return render(request, "home.html", {})

def Login_view(request, *args, **kwargs):
    return render(request, "login.html", {})

def Regsiter_view(request, *args, **kwargs):
    return render(request, "register.html", {})

@login_required
def Dashboard_view(request, *args, **kwargs):
    response = requests.get("http://127.0.0.1:8000/api/vehicle-violation-logs/")
    violations_list = response.json()
    return render(request, "dashboard.html", {"violations_list": violations_list})

def Detail_view(request, id, *args, **kwargs):
    url = f"http://127.0.0.1:8000/api/vehicle-violation-logs/{id}"
    response = requests.get(url)
    violation_details = response.json()
    return render(request, "violation.html", {"violation_details": violation_details})