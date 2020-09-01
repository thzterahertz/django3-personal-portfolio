from django.shortcuts import render
from .models import Project

#step 3 add Function
def home(request):
    projects =Project.objects.all()
    return render(request, 'portfolio/home.html', {'projects':projects})
