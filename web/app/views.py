from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from .forms import CustomUserCreationForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User



class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'




class UserListView(ListView):
    model = User
    template_name = 'user_list.html'