from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello world")

def foo(request):
    return HttpResponse("foo")

def woo(request):
    return HttpResponse("woo")
