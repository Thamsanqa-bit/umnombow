from django.shortcuts import render, redirect
from .models import Contact


# Create your views here.
def index(request):
    if request.method == 'POST':
        name = request.POST.get('name', "")
        email = request.POST.get('email', "")
        message = request.POST.get('message', "")
        user = Contact.objects.create(name=name, email=email, message=message)
        user.save()
        return redirect('/')
    return render(request, 'base/main.html')

def profile(request):
    return render(request, 'base/profile.html')

def services(request):
    return render(request, 'base/services.html')

def contact(request):
    return render(request, 'base/contact.html')
