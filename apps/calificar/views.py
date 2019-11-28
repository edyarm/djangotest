from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend

from .models import Professor, Student, Score
from .serializers import ProfessorSerializer, StudentSerializer, ScoreSerializer


class ProfessorViewset(viewsets.ModelViewSet):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['id', 'name']
    ordering_fields = ['id', 'name']


class StudentViewset(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['id', 'name']
    ordering_fields = ['id', 'name']


class ScoreViewset(viewsets.ModelViewSet):
    queryset = Score.objects.all()
    serializer_class = ScoreSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['id', 'name', 'value', 'student', 'professor']
    ordering_fields = ['id', 'name', 'value', 'student', 'professor']
