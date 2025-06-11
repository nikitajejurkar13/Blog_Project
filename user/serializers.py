from rest_framework import serializers
from .models import UserProfile
from django.contrib.auth.hashers import make_password, check_password

class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['username', 'email', 'password','role']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)

class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        try:
            user = UserProfile.objects.get(email=data['email'])
        except UserProfile.DoesNotExist:
            raise serializers.ValidationError("User not found")

        if not check_password(data['password'], user.password):
            raise serializers.ValidationError("Incorrect password")

        data['user'] = user
        return data

