from django.db import models

class For_test(models.Model):
    is_true = models.BooleanField()
    new_column = models.CharField(max_length=100, default=None, null=True)
