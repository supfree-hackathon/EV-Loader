from django.urls import path, include
from .views import HomePageView, SignUpView
from django.views.generic.base import TemplateView



urlpatterns = [
path('users/', include('django.contrib.auth.urls')),
path('', TemplateView.as_view(template_name='home.html'),name='home'),
path('signup/', SignUpView.as_view(), name='signup'),
]