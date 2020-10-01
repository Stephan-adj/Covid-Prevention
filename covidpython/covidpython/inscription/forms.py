from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import Utilisateur


class FormulaireInscription(UserCreationForm):

    class Meta(UserCreationForm):
        model = Utilisateur
        fields = ('email','is_superuser','nombre_foyer','nom','sexe_age_foyer','is_staff','adresse','code_postal','numero_telephone','allergie')



class ModificationFormulaire(UserChangeForm):

    class Meta:
        model = Utilisateur
        fields = ('email','is_superuser','nombre_foyer','nom','sexe_age_foyer','is_staff','adresse','code_postal','numero_telephone','allergie')
