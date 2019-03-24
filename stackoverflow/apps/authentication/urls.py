from django.urls import path
from rest_framework.authtoken import views

from .views import (RegisterAPIView, LoginView)

urlpatterns = [
    path('', RegisterAPIView.as_view(), name="register-newuser"),
    path('login/', LoginView.as_view()),
    path('gettoken/', views.obtain_auth_token)
]
