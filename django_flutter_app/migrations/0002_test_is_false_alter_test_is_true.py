# Generated by Django 4.2.2 on 2023-06-25 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_flutter_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='is_false',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='test',
            name='is_true',
            field=models.BooleanField(default=True),
        ),
    ]