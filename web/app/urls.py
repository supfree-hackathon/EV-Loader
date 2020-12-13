from django.urls import path, include
from .views import SignUpView, UserListView, UserSendTokensView
from django.views.generic.base import TemplateView




urlpatterns = [
path('users/', UserListView.as_view(), name='user_list'),
path('user/<int:pk>/send_tokens/', UserSendTokensView.as_view(), name='user_send_tokens'),
path('users/', include('django.contrib.auth.urls')),
path('', TemplateView.as_view(template_name='home.html'), name='home'),
path('signup/', SignUpView.as_view(), name='signup'),
path('UX1/', TemplateView.as_view(template_name='UX1.html')),
path('UX2/', TemplateView.as_view(template_name='UX2.html')),
path('UX3/', TemplateView.as_view(template_name='UX3.html')),
path('UX4/', TemplateView.as_view(template_name='UX4.html'))
]