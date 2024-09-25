from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Bienvenido a tu pagina")
    return render(request,'myapp/home.html')

def about(request):
    # return HttpResponse("Acerca de esta pagina")
    return render(request,'myapp/about.html')
def contact(request):
    # return HttpResponse("Pagina de contacto")
    return render(request,'myapp/contacto.html')
def service(request):
    # return HttpResponse("Pagina de servicios")
    return render(request,'myapp/service.html')
    
def blog(request):
    #  return HttpResponse("Pagina de blog")
    return render(request,'myapp/blog.html')
    
# Create your views here.
