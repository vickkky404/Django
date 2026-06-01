from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def myfunction(request):
    return HttpResponse('Hello Django')


def learn_math(request):
    a = 10+20
    return HttpResponse(a)
