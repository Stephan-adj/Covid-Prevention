# Generated by Django 3.0.5 on 2020-05-21 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inscription', '0006_auto_20200512_2309'),
    ]

    operations = [
        migrations.RenameField(
            model_name='utilisateur',
            old_name='nom_sexe_age_foyer',
            new_name='sexe_age_foyer',
        ),
        migrations.AddField(
            model_name='utilisateur',
            name='nom',
            field=models.CharField(default=None, max_length=500, verbose_name='Nom prénom'),
            preserve_default=False,
        ),
    ]
