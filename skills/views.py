from django.shortcuts import render

# Create your views here.

def display_skills(request):
    context = {'skills':'active'}
    return render(request, "skills/skills.html", context)
