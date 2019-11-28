from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=100)


class Professor(models.Model):
    name = models.CharField(max_length=100)


class Score(models.Model):
    name = models.CharField(max_length=100)
    value = models.FloatField()
    student = models.ForeignKey(Student, null=True, blank=True, on_delete=models.CASCADE)
    professor = models.ForeignKey(Professor, null=True, blank=True, on_delete=models.CASCADE)
