from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'index.html',{})


def contact_us(request):
    return render(request,'contact.html',{})


def blog(request):
    return render(request,'blog-details.html',{})