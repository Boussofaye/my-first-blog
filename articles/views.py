from django.shortcuts import render,redirect
from .models import Article
from django.contrib.auth import authenticate, login
from .forms import UserRegistrationForm, UserLoginForm
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Commande, UserProfile
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Créez vos vues ici.
def index(request):
    message = Article.objects.all()
    return render(request, "index.html", {"representant": message})

def acceuil(request):
    return render(request, "acceuil.html")

def proposer(request):
    return render(request, "propos.html")

def detail(request):  # Assurez-vous que cette fonction est bien indentée
    return render(request, "detail.html")

def beignetdetail(request):  # Assurez-vous que cette fonction est bien indentée
    return render(request, "beignetdetail.html")

def detailf(request):  # Assurez-vous que cette fonction est bien indentée
    return render(request, "detailf.html")

def detailh(request):  # Assurez-vous que cette fonction est bien indentée
    return render(request, "detailh.html")

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Rediriger vers la page de connexion
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request,username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('acceuil')  # Rediriger vers la page d'accueil
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form': form})

@csrf_exempt
@login_required
def create_order(request):
    if request.method == "POST":
        data = json.loads(request.body)
        produit = data.get("produit")
        prix = data.get("prix")

        # Enregistrer la commande
        commande = Commande.objects.create(
            utilisateur=request.user,
            produit=produit,
            prix=prix
        )

        return JsonResponse({"status": "success", "order_id": commande.id})
    return JsonResponse({"status": "not_logged_in"})

@login_required
def order_summary(request, order_id):
    # Récupérer la commande associée à l'utilisateur connecté
    commande = get_object_or_404(Commande, id=order_id, utilisateur=request.user)
    
    # Vérifie si un profil utilisateur existe, sinon en crée un
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    
    return render(request, 'order_summary.html', {
        'commande': commande,
        'user_profile': user_profile
    })
def user_beignet(request):  
    return render(request, "beignet.html")
def user_hemburger(request):  
    return render(request, "hemburger.html")
def user_fajita(request):  
    return render(request, "fajita.html")

@login_required
def mes_commandes(request):
    # Vérifier si l'utilisateur est superutilisateur
    if not request.user.is_superuser:
        messages.error(request, "Accès non autorisé.")
        return redirect('page_erreur')  # Redirige vers la page d'erreur
    
    commandes = Commande.objects.all()
    return render(request, 'mes_commandes.html', {'commandes': commandes})

@login_required
def supprimer_commande(request, commande_id):
    commande = get_object_or_404(Commande, id=commande_id)
    commande.delete()
    return redirect('mes_commandes') 

def page_erreur(request):
    return render(request, 'page_erreur.html')

