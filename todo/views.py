from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from todo import models
from todo.models import TODOO
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required(login_url='/loginn')
def home(request):
    return render(request, 'loginn.html')


def signup(request):

    if request.method == 'POST':
        fnm=request.POST.get('fnm')
        emailid=request.POST.get('emailid')
        pwd=request.POST.get('pwd')

        if User.objects.filter(username=fnm).exists():
            messages.error(request, 'Username is already taken')
        else:
            my_user=User.objects.create_user(username=fnm, email=emailid, password=pwd)
            my_user.save()
            print("Message added: Account created successfully!")
            return redirect('/loginn')
    
    return render(request, 'signup.html')
        

def loginn(request):
    if request.method == 'POST':
        fnm=request.POST.get('fnm')
        pwd=request.POST.get('pwd')
        print(fnm,pwd)
        userr=authenticate(request,username=fnm,password=pwd)
        if userr is not None:
            login(request,userr)
            return redirect('/todopage')
        else:
            messages.error(request, "No account found! Please sign up.")
            return redirect('/loginn')
               
    return render(request, 'loginn.html')
        
@login_required(login_url='/loginn')
def todo(request):
    if request.method == 'POST':
        title=request.POST.get('title')
        print(title)
        obj=models.TODOO(title=title,user=request.user)
        obj.save()
        user=request.user        
        res=models.TODOO.objects.filter(user=user).order_by('-date')
        return redirect('/todopage',{'res':res})
        
    
    res=models.TODOO.objects.filter(user=request.user).order_by('-date')
    return render(request, 'todo.html',{'res':res,})

def delete_todo(request,srno):
    print(srno)
    obj=models.TODOO.objects.get(srno=srno)
    obj.delete()
    return redirect('/todopage')

@login_required(login_url='/loginn')
def edit_todo(request, srno):
    if request.method == 'POST':
        title = request.POST.get('title')
        print(title)
        obj = models.TODOO.objects.get(srno=srno)
        obj.title = title
        obj.save()
        return redirect('/todopage')

    obj = models.TODOO.objects.get(srno=srno)
    return render(request, 'edit_todo.html', {'obj': obj})

def signout(request):
    logout(request)
    return redirect('/loginn')

