from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name=""),
    path('register',views.register,name="register"),
    path('login',views.login,name="login"),
    path('dashboard',views.dashboard,name="dashboard"),
    
]
