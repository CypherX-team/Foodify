from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')    

def donate(request):
    return render(request, 'donate.html')

def receive(request):
    return render(request, 'receive.html')

def signup(request):
    return render(request, 'signup.html')
