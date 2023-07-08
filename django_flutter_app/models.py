from django.db import models

class ForTest(models.Model):
    is_true = models.BooleanField(default=True)
    message = models.CharField(max_length=100, default='no message')

    class Meta:
        managed = True
        db_table = 'for_test'
