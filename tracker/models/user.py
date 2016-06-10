from django.db import models


class Job(models.Model):
    name = models.CharField(max_length=30)
    level = model.CharField(max_length=1, choices=(('0', 'trainee'), ('1', 'junior'), ('2', 'senior'), ('3', 'lead'), ('4', 'executive'),))
    division = model.CharField(max_length=1, choices=(('1', 'r&d'), ('2', 'consulting'), ('3', 'creative'), ('4', 'other'),))

class User(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=30)
    gender = models.CharField(max_length=1, choices=(('1', 'male'), ('2', 'female'), ('3', 'unknown'),))
    birthday = models.DateField()
    job = models.ForeignKey(Job, related_name="users")
