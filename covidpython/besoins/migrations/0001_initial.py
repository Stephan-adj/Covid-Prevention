# Generated by Django 3.0.5 on 2020-05-14 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Besoin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('allergie', models.CharField(max_length=10)),
                ('noms_allergies', models.CharField(max_length=100)),
                ('auxiliaire_vie', models.TextField(max_length=10)),
            ],
        ),
    ]