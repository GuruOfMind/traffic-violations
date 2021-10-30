from django.urls import include, path
from .views import *

urlpatterns = [
   path('', Home_view, name="home"),
   path('home/', Home_view, name="home"),
   path('login/', Login_view, name="login"),
   path('logout/', Logout_view, name="logout"),
   path('register/', Regsiter_view, name="register"),
   path('dashboard/', Dashboard_view, name="dashboard"),
   path('dashboard/violations/<int:id>/', Detail_view, name="detail"),
]