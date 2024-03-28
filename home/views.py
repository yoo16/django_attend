from django.shortcuts import render
from django.http import HttpResponse

# def index(request):
#     return HttpResponse("<p>Home</p>")

def index(request):
    context = {
        "heading": "Home",
    }
    return render(request, 'home/index.html', context)