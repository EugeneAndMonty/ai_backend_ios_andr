# Generated by Django 4.2.2 on 2023-07-05 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_flutter_app', '0005_for_test_new_column'),
    ]

    operations = [
        migrations.AlterField(
            model_name='for_test',
            name='new_column',
            field=models.CharField(default=None, max_length=100, null=True),
        ),
    ]