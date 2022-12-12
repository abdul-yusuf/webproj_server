from django.shortcuts import render

# Create your views here.

def HomeView(request):
    return render(request, 'core/home.html')

def CarearView(request):
    return render(request, 'core/carear.html')

def GallaryView(request):
    return render(request, 'core/gallary.html')