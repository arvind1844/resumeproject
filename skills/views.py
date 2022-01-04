from django.shortcuts import render

# Create your views here.

def display_skills(request):
    return render(request, "skills/skills.html")
