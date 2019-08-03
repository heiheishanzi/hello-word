from django.shortcuts import render
# from django.http import  HttpResponse

# Create your views here.
# def index(quest):
#     return  HttpResponse("hello")

def index(request):
    return  render(request,"index.html")