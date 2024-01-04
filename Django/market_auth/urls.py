from django.contrib import admin
from django.urls import path

from market_auth.views import login

urlpatterns = [
    path('login/', login),
]
