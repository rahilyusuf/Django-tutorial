from django.shortcuts import render
from django.http import HttpResponse

def index(request):
 context = {
  'name':'rahil',
  'age':'21',
 }
 return render(request,'index.html', context)

# Create your views here.