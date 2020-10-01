"""covidpython URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from inscription import views as v
from pageinternet import views as page
from polls import views as poll
from besoins import views as bes
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inscription/', v.inscription, name="inscription"),
	path('', page.Coming, name='coming'),
	path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('register/', v.inscription, name="inscription"),
    path('accounts/profile/', page.ProfileView.as_view(), name='profile'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  
	path('formulaire/completed', page.ProfileView.as_view(), name='profile'),
	path('profile/', page.ProfileView.as_view(), name='profile'),
	path('formulaire/', bes.definir_besoin, name='formulaire'),
	#Polls url
	path('poll/', poll.PollListView.as_view(), name='blog-home'),
    path('post/<int:pk>/', poll.PollDetailView.as_view(), name='post-detail'),
    path('post/new/', poll.PollCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', poll.PollUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', poll.PollDeleteView.as_view(), name='post-delete'),
    path('about/', poll.AboutView.as_view(), name='blog-about'),
]
