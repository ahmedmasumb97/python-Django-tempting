from django.urls import path
from  .import views


urlpatterns = [
    path('hello/',views.say_hello),
    path('home/', views.htmlpage),
    path('about/', views.about),
    path('contact/', views.contact),
    path('history/', views.history),
    path('experiment/', views.experiment),
    path('experiment/<person>', views.experiment),
     path('experiment/<person>/greeting/<greet>/', views.experiment_greet),
  
  
    
]
