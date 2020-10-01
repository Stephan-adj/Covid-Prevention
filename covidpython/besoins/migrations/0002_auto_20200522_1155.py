# Generated by Django 3.0.5 on 2020-05-22 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('besoins', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='besoin',
            name='maladie_chronique',
            field=models.CharField(default=None, max_length=3, verbose_name='Avez-vous une maladie chronique'),
        ),
        migrations.AddField(
            model_name='besoin',
            name='noms_maladie_chronique',
            field=models.CharField(blank=True, default=None, max_length=150, null=True, verbose_name='Si vous avez une maladie chronique, quelle-est-elle ? '),
        ),
        migrations.AddField(
            model_name='besoin',
            name='why_auxiliaire_vie',
            field=models.CharField(blank=True, default=None, max_length=150, null=True, verbose_name="Pourquoi avez-vous besoin d'un(e) auxiliaire de vie ? "),
        ),
        migrations.AlterField(
            model_name='besoin',
            name='allergie',
            field=models.CharField(default=None, max_length=3, verbose_name='Avez-vous une allergie'),
        ),
        migrations.AlterField(
            model_name='besoin',
            name='auxiliaire_vie',
            field=models.CharField(default=None, max_length=3, verbose_name="Avez-vous besoin d'un(e) auxiliaire de vie"),
        ),
        migrations.AlterField(
            model_name='besoin',
            name='noms_allergies',
            field=models.CharField(blank=True, default=None, max_length=150, null=True, verbose_name='Si vous avez une allergie, quelle-est-elle ? '),
        ),
    ]