from django.db import models
from django.contrib.auth.models import User

# Modèle pour les articles
class Article(models.Model):
    titre = models.CharField(max_length=30)
    resume = models.CharField(max_length=100)
    contenu = models.TextField(blank=True)
    date_edition = models.DateTimeField(auto_now_add=False)

    def __str__(self):
        return f"{self.titre}"

# Modèle pour le profil utilisateur
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    numero_telephone = models.CharField(max_length=15, null=True, blank=True)
    adresse_rue = models.CharField(max_length=100, null=True, blank=True)
    nom_prenom = models.CharField(max_length=255, null=True, blank=True)



class Commande(models.Model):
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE)
    produit = models.CharField(max_length=100)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"Commande de {self.utilisateur.username} - {self.produit}"