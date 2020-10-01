from django import forms
from .models import Besoin

class FormulaireBesoin(forms.ModelForm):

    class Meta:
        model = Besoin
        fields = ('email', 'allergie', 'maladie_chronique', 'auxiliaire_vie', 'noms_allergies','noms_maladie_chronique','why_auxiliaire_vie')

    

    
