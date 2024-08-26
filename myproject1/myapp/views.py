from django.shortcuts import render 
from django.http import  HttpResponse


# Create your views here.

def say_hello(request):
    return HttpResponse("Hello! Django")

# def homepage(request):
#     return HttpResponse("Welcome! Homepage")

def htmlpage(request):
    data ={
        "name":"Home Page",
        "content":"Welcom to our home page"
        }
    return  render(request,'index.html',context=data)


def about(request):
    data ={
        "name":"About Page",
        "content":"Welcom to our about page"
        }
    return render(request,'about.html',context=data)


def contact(request):
    data ={
        "name":"Contact Page",
        "content":"Welcom to our  page"
        }
    email = "ahmedmasum.b97@gmail.com"
    phone = '01776050586'
    social_address = ["facebook: ahmedmasum@facebook.com", "instagram: masum.instagram.com","youtube: techahmedbd.youtube"]
    hq = 'd'
    return render(request,'contact.html',context= {"emailaddress":email,"phonenumber":phone,'social_profile':social_address,'hq':hq,'data':data})



def  history(request):
    data ={
        "name":"History Page",
        "content":"Welcom to history page"
        }
    
    return render(request,'history.html',context=data)


def experiment(request,person=None):
    if person is None:
        person = "Hi! Guest"
        
    return render(request,'experiment.html',{"data":person})

def experiment_greet(request,person,greet):
 
    return render(request,'experiment.html',{"data":person,"greeting":greet})
