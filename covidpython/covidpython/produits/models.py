from django.db import models

# Create your models here.
class Produit(models.Model):
    nom = models.CharField(max_length=50)
    demande = models.IntegerField()
    stock= models.IntegerField()
    
    def __str__(self):
        return self.nom
