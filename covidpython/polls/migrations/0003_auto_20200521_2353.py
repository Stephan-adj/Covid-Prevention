# Generated by Django 3.0.5 on 2020-05-21 21:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20200521_1852'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='poll',
            name='is_anonymous',
        ),
        migrations.RemoveField(
            model_name='poll',
            name='is_authenticated',
        ),
    ]