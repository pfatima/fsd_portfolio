from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'fatima_portfolio/index.html')
def about(request):
    return render(request, 'fatima_portfolio/about.html')
def resume(request):
    return render(request, 'fatima_portfolio/resume.html')