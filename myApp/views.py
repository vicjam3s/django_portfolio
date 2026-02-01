from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'myApp/index.html')

def about(request):
    return render(request, 'myApp/about.html')


def projects(request):
    return render(request, 'myApp/projects.html')


def contact(request):
    return render(request, 'myApp/contacts.html')