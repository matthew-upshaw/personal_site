from django.shortcuts import render
from . models import Publication

def home_page(request):
    context = {}

    return render(request, 'home_page.html', context)

def publication_page(request):
    publications = Publication.objects.all().order_by('-year')

    context = {
        'publications': publications,
    }

    return render(request, 'publication_page.html', context)
