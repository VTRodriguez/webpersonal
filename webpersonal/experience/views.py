from django.shortcuts import render
from .models import Project

# Create your views here.

def experience(request):
    projects = Project.objects.all()
    return render(request, "experience/experience.html", {'projects': projects})