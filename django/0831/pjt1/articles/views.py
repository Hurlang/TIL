from django.shortcuts import render

# Create your views here.
def catch(request):
    return render(request, 'articles/catch.html')

def index(request):
    return render(request, 'articles/index.html')