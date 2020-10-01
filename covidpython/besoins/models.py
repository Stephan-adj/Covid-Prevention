from django.db import models

class Besoin(models.Model):
    email=why_auxiliaire_vie = models.EmailField("Entrez votre adresse email svp", null=False)
    allergie = models.BooleanField(('Avez-vous une allergie ?'), default=None,max_length=3)
    maladie_chronique = models.BooleanField(('Avez-vous une maladie chronique ?'), default=None,max_length=3)
    auxiliaire_vie = models.BooleanField(("Avez-vous besoin d'un(e) auxiliaire de vie ?"), default=None,max_length=3)
    noms_allergies = models.CharField(("Si vous avez une allergie, quelle-est-elle ? "), default=None,blank=True,null=True,max_length=150)
    noms_maladie_chronique = models.CharField(("Si vous avez une maladie chronique, quelle est-elle ? "), default=None,blank=True,null=True,max_length=150)
    why_auxiliaire_vie = models.CharField("Pourquoi avez-vous besoin d'un(e) auxiliaire de vie ? ", default = None,blank=True,null=True,max_length=150)

    def __str__(self):
        return self.email