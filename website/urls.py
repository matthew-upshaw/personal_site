from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home-page'),
    path('education/', views.education_page, name='education-page'),
    path('experience/', views.experience_page, name='experience-page'),
    path('research/publications/', views.publication_page, name='publication-page'),
]
