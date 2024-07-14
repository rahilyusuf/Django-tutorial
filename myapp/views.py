from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http import HttpResponse
from . models import Feature

def index(request):
 features = Feature.objects.all()
 return render(request,'index.html',{'features':features})

def counter(request):
 text = request.POST['text']
 amount_of_words = len(text.split())
 return render(request, 'counter.html', {'amount':amount_of_words} )

def register(request):
 if request.method == 'POST':
  username=request.POST['Username']
  email=request.POST['email']
  password=request.POST['password']
  password2=request.POST['password2']
  
  if password == password2:
   if User.objects.filter(email=email):
    messages.info(request,'Email Already used')
    return redirect('register')
   
   elif User.objects.filter(username=username):
    messages.info(request,'username already used')
    return redirect('register')
   
   else:
    user=User.objects.create_user(username=username, email=email, password=password)
    user.save();
    return redirect('login')
   
  else:
   messages.info(request,'Pasword not Matching')
   return redirect('register')
 else:
  return render(request,'register.html')

# Create your views here.