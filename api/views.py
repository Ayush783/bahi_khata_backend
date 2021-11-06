from django.http import HttpResponse
from django.http.response import JsonResponse

# Create your views here.

def welcome(request):
    return JsonResponse(data={'message':'Welcome to bahi khata api'})

def register(request,id):
    pass

def userdata(request,id):
    pass
