from django.contrib import admin
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import FormulaireInscription, ModificationFormulaire
from .models import Utilisateur


class Admin(UserAdmin):
    add_form = FormulaireInscription
    form = ModificationFormulaire
    model = Utilisateur
    list_display = ('email', 'is_staff', 'is_active', 'is_superuser')
    list_filter = ('email', 'is_staff', 'is_active', 'is_superuser')
    fieldsets = (
        (None, {'fields': (
        'email', 'nombre_foyer', 'nom_sexe_age_foyer', 'adresse', 'code_postal', 'numero_telephone', 'allergie')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
            'email', 'nombre_foyer', 'nom_sexe_age_foyer', 'adresse', 'code_postal', 'numero_telephone', 'allergie')}
         ),
    )
    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(Utilisateur, Admin)
