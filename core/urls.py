
from django.urls import path

from core import views

urlpatterns = [
    path("",views.HomeView, name="home"),
    path("signup/",views.Signup, name="signup"),
]
