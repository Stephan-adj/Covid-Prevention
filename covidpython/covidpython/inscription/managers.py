from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _


class GestionUtilisateur(BaseUserManager):

    def create_user(self, email, password, **autre_champ):
        if not email:
            raise ValueError(_('Entrez une adresse email'))
        email = self.normalize_email(email)
        user = self.model(email=email, **autre_champ)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **autre_champ):
        autre_champ.setdefault('is_staff', True)
        autre_champ.setdefault('is_superuser', True)
        autre_champ.setdefault('is_active', True)

        if autre_champ.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if autre_champ.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **autre_champ)
