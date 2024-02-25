from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.get_users),
    path('users/register/', views.register_user),
]
