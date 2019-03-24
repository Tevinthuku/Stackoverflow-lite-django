from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "password",
            "password2"
        ]

    def validate_email(self, email):
        query_set = User.objects.filter(email__iexact=email)
        if query_set.exists():
            raise serializers.ValidationError(
                "user with this email already exists")
        return email

    def validate_username(self, username):
        query_set = User.objects.filter(username__iexact=username)
        if query_set.exists():
            raise serializers.ValidationError(
                "user with this username already exists")
        return username

    def validate(self, data):
        pw = data.get("password")
        pw2 = data.get("password2")

        if pw != pw2:
            raise serializers.ValidationError("Passwords do not match")

        return data

    def create(self, vallidated_data):
        user_object = User(username=vallidated_data.get(
            "username"), email=vallidated_data.get("email"))
        user_object.set_password(vallidated_data.get("password"))
        user_object.save()
        return user_object


class LoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=255)
    username = serializers.CharField(max_length=255, read_only=True)
    password = serializers.CharField(max_length=128, write_only=True)
