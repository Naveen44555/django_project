from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.db import connection
import json
from django.views.decorators.csrf import csrf_exempt 
from basic.models import Students
from .models import postsdata
# from .models import employees

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

def health(request):
    try:
        with connection.cursor() as c:
            c.execute("SELECT 1")
        return JsonResponse({"status":"ok","db":"connected"})
    except Exception as e:
        return JsonResponse({"status":"error","db":str(e)})
    


# to test database connection
@csrf_exempt
def addstudent(request):
    print(request.method)
    if request.method == 'POST':   # ✅ must be uppercase
        # try:
            data = json.loads(request.body)
            students = Students.objects.create(  # ✅ lowercase 'objects'
                name=data.get('name'),
                age=data.get('age'),
                email=data.get('email')
            )
            return JsonResponse({"status": "success", "id": students.id}, status=200)
        # except Exception as e:
    elif request.method  =="GET": 
        result = list(Students.objects.values())
        print(result)
        return JsonResponse({"status":"ok","data":result},status=200)
    elif request.method =="PUT":
        data = json.loads(request.body)
        ref_id =data.get("id")  #getting id
        new_email=data.get("email")  #getting email
        existing_student=students.objects.get(id=ref_id)
        existing_student.email=new_email
        existing_student.save()
        # print(existing_student)

        return JsonResponse({"req":"put method requested"},status=200)
    
    elif request.method == "DELETE":
        return JsonResponse({"req":"delete method requested"},status=200)
            # return JsonResponse({"status": "error", "message": str(e)}, status=400)
    return JsonResponse({"error": "Use POST method"}, status=400)


# @csrf_exempt
# def employeedata(request):
#     print(request.method)
#     if request.method == "POST":
#         data = json.loads(request.body)
#         new=employees.object.create(ename=data.get('ename'),age= data.get("age"),email=data.get("email"),salary=data.get("salary")
#         return JsonResponse ({"status":"success","id":newpost.id},status=200)
#         )



@csrf_exempt
def new(request):
    if request.method == "POST":
        try:
            data=json.loads(request.body)
            newpost = postsdata.objects.create(
                post_name=data.get('post_name'),
                post_type=data.get('post_type'),
                post_date=data.get('post_date'),
                post_content=data.get('post_content')
            )
            return JsonResponse({"status":"success","id":newpost.id},status=200)
        except Exception as e:

            return JsonResponse({"error":str(e)},status=400)
    return JsonResponse({"error": "Only POST method allowed"}, status=405)



