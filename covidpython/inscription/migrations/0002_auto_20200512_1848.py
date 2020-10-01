# Generated by Django 3.0.5 on 2020-05-12 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inscription', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='utilisateur',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='Adresse email'),
        ),
        migrations.AlterField(
            model_name='utilisateur',
            name='nom_sexe_age_foyer',
            field=models.CharField(max_length=500, verbose_name='Nom prénom age sexe de chaque personne'),
        ),
        migrations.AlterField(
            model_name='utilisateur',
            name='nombre_foyer',
            field=models.IntegerField(default=None, verbose_name='Nombre de personnes dans le foyer'),
        ),
        migrations.AlterField(
            model_name='utilisateur',
            name='numero_telephone',
            field=models.IntegerField(default=None, verbose_name='numéro de téléphone'),
        ),
    ]