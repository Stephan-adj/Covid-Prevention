from django.shortcuts import render, redirect, reverse
from django.views import View
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import PermissionDenied
from django.contrib.auth.mixins import LoginRequiredMixin
from django import *
# Create your views here.

#class Formulaire(LoginRequiredMixin, View):
#	def get(self, request):
#		return render(request, 'formulaire.html')

def Coming(request):
	return render(request, 'coming.html')
	
def Login(request):
	return render(request, 'login.html')
	
class ProfileView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'profile.html')
		
class LoginView(View):
	def get(self, request):
		return render(request, 'login.html', {form: authenticate})
	