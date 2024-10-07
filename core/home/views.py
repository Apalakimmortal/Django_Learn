from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    peoples =[
        {'name': 'Apalak Rajesh' , 'age' : 21},
        {'name': 'Kavya Srivastava' , 'age' : 16},
        {'name': 'Manan Kaushik' , 'age' : 24 },
        {'name': 'Aman Kumar' , 'age' : 22},
    ]
    return render(request,'home/index.html',context={'peoples' : peoples})

def success_page(request):
    return HttpResponse("Hey this is a success page")

def about(request):
    return render(request,'home/about.html')

def contact(request):
    return render(request,'home/contact.html')