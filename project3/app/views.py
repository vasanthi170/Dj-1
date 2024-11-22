from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def kumari(request):
    return HttpResponse('vanakkam anjali kumari deviiiii')

def vasu(request):
    return HttpResponse('<h1>Hello people! Tomorrow is thursday</h1>')

def srav(request):
    return HttpResponse('<h1><marcue></marcue></h1>')
