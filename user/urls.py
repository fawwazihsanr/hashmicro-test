from django.urls import path
from . import views

urlpatterns = [
    path('login', views.user_login, name='login'),
    path('login-as-guest', views.login_as_guest, name='login-as-guest'),
    path('logout', views.user_logout, name='logout'),
]