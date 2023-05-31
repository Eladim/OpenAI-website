from django.urls import path
from . import views

app_name = 'users'  # same as what you've used in your templates' paths

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
]
