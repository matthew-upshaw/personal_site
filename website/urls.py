from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home-page'),
    path('research/publications/', views.publication_page, name='publication-page'),
]
