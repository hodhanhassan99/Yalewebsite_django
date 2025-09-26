from tkinter.font import names

from django.shortcuts import render,redirect
from .models import Upload


# Create your views here.
def home(request):
    return render(request, 'index.html')
def about(request):
    return render(request, 'about.html')
def contact(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        message=request.POST.get('message')

        query=Upload(name=name,email=email,subject=subject,message=message)
        query.save()
        return redirect('/')
    return render(request, 'contact.html')
def properties(request):
    return render(request, 'properties.html')
def services(request):
    return render(request,'services.html')
def agents(request):
    return render(request,'agents.html')
