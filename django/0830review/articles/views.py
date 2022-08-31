from multiprocessing import context
from django.shortcuts import render

# Create your views here.
def index(request):
    text = request.GET.get('text')
    print(text)
    context = {
        'text' : text
    }
    return render(request, 'index.html', context)


def dinner(request):
    return render(request, 'dinner.html')