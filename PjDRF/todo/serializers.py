from rest_framework import serializers
from .models import Projects, ToDo


class ProjectsSerializerBase(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ['title', 'users']


class ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = '__all__'


class ToDoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDo
        fields = '__all__'
