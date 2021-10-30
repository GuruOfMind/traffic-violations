from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
import requests
from django.contrib import messages

def Home_view(request, *args, **kwargs):
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
        response = requests.post("https://e-traffic-violations.herokuapp.com//api/vehicles/", data=payload)
        if response.status_code == 201:
            data = response.json()
            return redirect("login")
        else:
            print(response.content)
            return redirect("home")
    return render(request, "register.html", {})
        
@login_required(login_url="/login")
def Dashboard_view(request, *args, **kwargs):
    current_user = request.user
    vehicle_url = f"https://e-traffic-violations.herokuapp.com//api/vehicles/{current_user.username}/" 
    user_driver = requests.get(vehicle_url).json()
    response = requests.get(f"https://e-traffic-violations.herokuapp.com//api/vehicle-violation-logs/?plugged_number={user_driver['plugged_number']}&driver={user_driver['driver']}&is_paid=false")
    violations_list = response.json()
    return render(request, "dashboard.html", {"violations_list": violations_list})

@login_required(login_url="/login")
def Detail_view(request, id, *args, **kwargs):
    url = f"https://e-traffic-violations.herokuapp.com//api/vehicle-violation-logs/{id}"
    response = requests.get(url)
    violation_details = response.json()
    return render(request, "violation.html", {"violation_details": violation_details})

@login_required(login_url="/login")
def Payment_view(request, id, *args, **kwargs):
    url = f"https://e-traffic-violations.herokuapp.com//api/vehicle-violation-logs/{id}/"
    response = requests.patch(url, data={"is_paid":True})
    if response.status_code == 200:
        messages.add_message(request, messages.INFO, 'Violation has been paid successfully')
        return redirect("dashboard")
    messages.add_message(request, messages.error, 'Violation has been paid successfully')
    return redirect('dashboard')