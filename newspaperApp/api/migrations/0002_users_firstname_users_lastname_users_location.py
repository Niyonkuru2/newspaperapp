# Generated by Django 5.0.6 on 2024-11-05 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='firstName',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='users',
            name='lastName',
            field=models.CharField(max_length=70, null=True),
        ),
        migrations.AddField(
            model_name='users',
            name='location',
            field=models.CharField(max_length=50, null=True),
        ),
    ]