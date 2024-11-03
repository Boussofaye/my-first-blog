from django import forms
from django.contrib.auth.models import User
from .models import UserProfile

class UserRegistrationForm(forms.ModelForm):
    nom_prenom = forms.CharField(
        max_length=100, 
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    numero_telephone = forms.CharField(
        max_length=15, 
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    adresse_rue = forms.CharField(
        max_length=100, 
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    
    class Meta:
        model = User
        fields = ['username', 'nom_prenom','numero_telephone', 'adresse_rue', 'password']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
            UserProfile.objects.create(
                user=user,
                numero_telephone=self.cleaned_data['numero_telephone'],
                adresse_rue=self.cleaned_data['adresse_rue'],
                nom_prenom=self.cleaned_data['nom_prenom']
            )
        return user


class UserLoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))