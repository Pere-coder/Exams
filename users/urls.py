from .views import sign_up, login
from django.urls import path



urlpatterns = [
    path('signup', sign_up, name='signup'),
    path('login', login, name='login'),
]