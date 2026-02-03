from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'pages/index.html')

def about(request):
    return render(request, 'pages/about.html')


def projects(request):
    return render(request, 'pages/projects.html')


def contact(request):
    return render(request, 'pages/contacts.html')