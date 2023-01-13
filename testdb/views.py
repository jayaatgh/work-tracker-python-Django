from django.shortcuts import render,HttpResponse, redirect
from .models import register, fileupload 
import os
from django.conf import settings
from django.http import HttpResponse, Http404


# Create your views here.
def registerdata(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        address = request.POST.get('address')
        username = request.POST.get('username')
        password = request.POST.get('password')
        users = register()
        users.Name = name
        users.Address = address
        users.Username = username
        users.Password = password
        users.save()
    return render(request,'registerpage.html')

def userlog(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            register.objects.get(Username=username,Password=password)
            return redirect('/upload')
        except:
            return HttpResponse('Invalid User')
    return render(request,'userlogin.html')

def adminlog(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username == 'admin' and password == 'admin':
            return redirect('/pending')
        else:
            return HttpResponse('Invalid')
    return render(request, 'adminlogin.html')

def pending(request):
    details = register.objects.filter(Status=False)
    return render(request,'pendinglist.html',{'value':details})

def approved(request):
    details = register.objects.filter(Status=True)
    return render(request,'approvedlist.html',{'value':details})

def approve(request,id):
    data = register.objects.get(id=id)
    data.Status = True
    data.save()
    return redirect('/pending')

def edit(request,id):
    details = register.objects.filter(Status=True)
    users = register.objects.get(id=id)
    if request.method == 'POST':
        address = request.POST.get('address')
        password = request.POST.get('password')
        users.Address = address
        users.Password = password
        users.save()
        return redirect('/approved')
    return render(request,'approvedlist.html',{'value':details,'value1':users})

def delete(request,id):
    data = register.objects.filter(id=id).delete()
    return redirect('/approved')

def upload(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        designation = request.POST.get('designation')
        file = request.FILES['file']
        data = fileupload()
        data.Name = name
        data.Designation = designation
        data.File = file
        data.save()
    return render(request,'uploadfile.html')

def img_view(request):
    details = fileupload.objects.all()
    return render(request,'imageview.html',{'value':details})


