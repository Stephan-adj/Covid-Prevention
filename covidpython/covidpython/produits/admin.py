from django.contrib import admin
from django.contrib.auth.models import Group
#from django.contrib.auth.models import User
from .models import Produit
# Register your models here.

admin.site.site_header ="Interface"
class ProduitAdmin(admin.ModelAdmin):
    list_display = ('nom', 'demande', 'stock')

admin.site.register(Produit, ProduitAdmin)
admin.site.unregister(Group)
#admin.site.unregister(User)