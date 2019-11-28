from rest_framework import serializers
from .models import Professor, Student, Score


class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = ('id', 'name')
        ordering = ('id', 'name')


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('id', 'name')
        ordering = ('id', 'name')


class ScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Score
        fields = ('id', 'name', 'value', 'student', 'professor')
        ordering = ('id', 'name', 'value', 'student', 'professor')
