from django.shortcuts import render
from django.http import HttpResponse

def index(request):
 context = {
  'name':'rahil',
  'age':'21',
 }
 return render(request,'index.html')

def counter(request):
 text = request.POST['text']
 amount_of_words = len(text.split())
 return render(request, 'counter.html', {'amount':amount_of_words} )

# Create your views here.