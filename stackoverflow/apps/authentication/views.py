from rest_framework import generics
from django.db.models import Q
from rest_framework.response import Response

from django.contrib.auth import (get_user_model, authenticate)


from .serializers import (UserRegistrationSerializer, LoginSerializer)

User = get_user_model()


class RegisterAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer


class LoginView(generics.CreateAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        data = request.data
        email = data.get("email")
        username = data.get("username")
        password = data.get("password")
        authenticate(username=username, password=password)
        qs = User.objects.filter(
            Q(username__iexact=username) | Q(email__iexact=email)
        ).distinct()
        print(qs)
        if qs.count() == 1:
            user_obj = qs.first()
            if user_obj.check_password(password):
                return Response({"data": "Authenticated correctly",
                                 "user": LoginSerializer(user_obj).data})
            return Response({"detail": "Incorrect password"}, status=400)
        return Response({"detail": "You are not a user"}, status=404)
