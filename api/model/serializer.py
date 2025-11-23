from rest_framework import serializers
from .models import TeachersData, StudentsData
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator

class StudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentsData
        fields = "__all__"


class TeachersSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeachersData
        fields = "__all__"

class UserRegisterSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all(), message="Este email ya está en uso.")]
    )
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {"password":{'write_only':True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            username = validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user
