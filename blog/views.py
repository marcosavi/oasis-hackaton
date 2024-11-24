from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "blog/index.html", {})

def translanguaging(request):
    return render(request, "blog/translanguaging.html", {})

def arabizi(request):
    return render(request, "blog/translanguaging.html", {})

def codeswitching(request):
    return render(request, "blog/translanguaging.html", {})

def whitedialects(request):
    return render(request, "blog/translanguaging.html", {})