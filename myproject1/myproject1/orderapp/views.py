from django.shortcuts import render
from django.http import  HttpResponse

# Create your views here.




def orders(request):
    data ={
        "name":"Contact Page",
        "content":"Welcom to our  page"
        }
    return render( request, 'demo.html',data)