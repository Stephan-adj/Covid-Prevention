# Generated by Django 3.0.5 on 2020-05-12 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inscription', '0004_auto_20200512_2055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='utilisateur',
            name='nom',
            field=models.CharField(max_length=500, verbose_name='Nom prénom'),
        ),
        migrations.AlterField(
            model_name='utilisateur',
            name='sexe_age_foyer',
            field=models.CharField(max_length=500, verbose_name='Age sexe de chaque personne'),
        ),
    ]
