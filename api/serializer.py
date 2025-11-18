from rest_framework import serializers
from .models import TeachersData, StudentsData


class StudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentsData
        fields = "__all__"


class TeachersSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeachersData
        fields = "__all__"
