from django.shortcuts import render
from . models import Education, Publication

def home_page(request):
    context = {}

    return render(request, 'home_page.html', context)

def publication_page(request):
    publications = Publication.objects.all().order_by('-year')

    context = {
        'publications': publications,
    }

    return render(request, 'publication_page.html', context)

def education_page(request):
    educations = Education.objects.all().order_by('graduation_date')

    context = {
        'educations': educations,
    }

    return render(request, 'education_page.html', context)
