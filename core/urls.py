
from django.urls import path

from core import views

urlpatterns = [
    path("",views.HomeView, name="home"),
    path("signup/",views.Signup, name="signup"),
    path('secret/', views.secret_page, name="secret"),
    path('secret2/', views.SecretView2.as_view(), name="secret2"),

]
