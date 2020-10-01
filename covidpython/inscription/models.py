from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _

from .managers import GestionUtilisateur


class Utilisateur(AbstractBaseUser, PermissionsMixin):
	email = models.EmailField(_('Adresse email'), unique=True)
	nombre_foyer = models.IntegerField(_('Nombre de personnes dans le foyer'),default=None,)
	adresse = models.CharField(max_length=150)
	code_postal = models.IntegerField(default=None)
	numero_telephone = models.IntegerField(_('numéro de téléphone'),default=None)
	nom = models.CharField(_('Nom prénom'),max_length=500)
	sexe_age_foyer = models.CharField(_('Age sexe de chaque personne'),max_length=500)
	allergie = models.BooleanField(default=False)
	is_staff = models.BooleanField(default=False)
	is_superuser = models.BooleanField(default=False)
	is_active = models.BooleanField(default=True)

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = []

	objects = GestionUtilisateur()

	def __str__(self):
		return self.email
# Create your models here.
