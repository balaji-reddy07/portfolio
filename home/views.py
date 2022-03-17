from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("this is the project(/)")

about = lambda request : HttpResponse("<h1>About page</h1>")