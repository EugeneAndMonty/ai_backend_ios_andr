from django.db import models

class For_test(models.Model):
    is_true = models.BooleanField()

class For_friends(models.Model):
    name = models.CharField(max_length=20)