# Generated by Django 3.0.5 on 2020-05-12 21:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inscription', '0005_auto_20200512_2112'),
    ]

    operations = [
        migrations.RenameField(
            model_name='utilisateur',
            old_name='sexe_age_foyer',
            new_name='nom_sexe_age_foyer',
        ),
        migrations.RemoveField(
            model_name='utilisateur',
            name='nom',
        ),
    ]
