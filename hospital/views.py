from django.shortcuts import render,redirect
from hospital.models import *
from django.http import HttpResponse

# Create your views here.
def test(request):
    return HttpResponse('Checking the Page')
    
def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def treatment(request):
    return render(request,'treatment.html')
def contact(request):
    return render(request,'contact.html')
def doctor(request):
    return render(request,'doctor.html')
def signup(request):
    return render(request,'signup.html')
def login(request):
    return render(request,'login.html')
def bloodbank(request):
    return render(request,'bloodbank.html') 
def sign(request):
    c=client()
    c.Firstname=request.GET['Firstname']
    c.lastname=request.GET['lastname']
    c.email=request.GET['email']
    c.password=request.GET['password']
    c.save()
    return render(request,'index.html')

def log(request):
    email1=request.GET['email']
    password1=request.GET['password']
    if client.objects.filter(email= email1,password=password1):
        return render(request,'index.html')
    else:
        return render(request,'login.html') 

def apoint(request):
    a=appointment()
    a.patient=request.GET['patient']
    a.doctor=request.GET['doctor']
    a.dept=request.GET['dept']
    a.phn=request.GET['phn']
    a.smpt=request.GET['smpt']
    a.save()
    return render(request,'index.html')

def donor(request):
    d=bloodbank()
    d.name=request.GET['name']
    # d.bloodtype=request.GET['bloodtype']
    d.phone=request.GET['phone']
    # d.firsttime=request.GET['firsttime']
    d.save()
    return render(request,'bloodbank.html')