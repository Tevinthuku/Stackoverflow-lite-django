from django.urls import path

from .views import (RegisterAPIView, LoginView)

urlpatterns = [
    path('', RegisterAPIView.as_view(), name="register-newuser"),
    path('login/', LoginView.as_view())
]
