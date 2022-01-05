from django.shortcuts import render

# Create your views here.

def display_eduexp(request):
    context = {'eduexp':'active'}
    return render(request, "eduexp/eduexp.html", context)
