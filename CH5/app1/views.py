from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.



# views is the file where the business logic is written.
# so this is the example of the views written without using any AI.
# def myfunction(request):
#     return HttpResponse('Hello Django')


# def learn_math(request):
#     a = 10+20
#     return HttpResponse(a)

def home(request):
    return HttpResponse('Home Page')

def myapp1(request):
    return HttpResponse('My  App Page')