from .forms import FormulaireBesoin
from .models import Besoin
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
#from inscription.models import Utilisateur

class Admin(UserAdmin):
    add_form = FormulaireBesoin
    model = Besoin
    fieldsets = (
        (None, {'fields': (
        'email','allergie', 'maladie_chronqiue', 'auxiliaire_vie', 'noms_allergies', 'noms_maladie_chronique', 'why_auxiliaire_vie')}),
        
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
            'email', 'allergie', 'maladie_chronqiue', 'auxiliaire_vie', 'noms_allergies', 'noms_maladie_chronique', 'why_auxiliaire_vie')}
         ),
    )
    search_fields = ('email',)
    ordering = ('email',)

#admin.site.unregister(Utilisateur)
admin.site.register(Besoin)