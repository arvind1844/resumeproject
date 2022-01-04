from django.shortcuts import render

# Create your views here.

def display_eduexp(request):
    return render(request, "eduexp/eduexp.html")
