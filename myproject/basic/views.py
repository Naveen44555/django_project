from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
# Create your views here.

def sample(request):
    return HttpResponse('hello world')

def sample1(request):
    return HttpResponse('welcome to django')

def sampleInfo(request):
    # data={"name":"naveen",'age':23,'city':'hyd'}
    data={'result':[2,4,5,6]}
    return JsonResponse(data)

def dynamicResponse(request):
    name=request.GET.get("name",'honey')
    city=request.GET.get("city",'hyd')

def add(request):
    a=request.GET.get("a",5)
    b=request.GET.get('b',4)
    result=a+b
    return HttpResponse(f"sum of {a} and {b} is {result}")
   

def mult(request):
    c=request.GET.get("c",10)
    d=request.GET.get("d",4)
    result1=int(c)*int(d)
    return HttpResponse(f"mult of values {c} and {d} are {result1}")

def sub(request):
    e=request.GET.get("e",8)
    f=request.GET.get("f",5)
    result=e-f
    return HttpResponse(f"sub of values {e}-{f} = {result}")

def div(request):
    g=request.GET.get("g",9)
    h=request.GET.get("h",3)
    result=g//h
    return HttpResponse(f"div of values{g}/{h}={result}")
