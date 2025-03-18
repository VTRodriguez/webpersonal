from django.shortcuts import render
from .models import Project
from .models import Hobby

# Create your views here.

def about_me(request):
    projects = Project.objects.all()
    hobbies = Hobby.objects.all()
    return render(request, "about_me/about_me.html", {'projects': projects, 'hobbies': hobbies})