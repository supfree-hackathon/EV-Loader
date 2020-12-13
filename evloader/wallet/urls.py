from django.urls import path

from . import views

urlpatterns = [
    path('sup-points', views.handle_sup_points),
]