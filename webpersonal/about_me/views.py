from django.shortcuts import render
from .models import Project

# Create your views here.

def about_me(request):
    projects = Project.objects.all()
    return render(request, "about_me/about_me.html", {'projects': projects})