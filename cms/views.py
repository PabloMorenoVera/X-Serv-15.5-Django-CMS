from django.shortcuts import render
from django.http import HttpResponse
from .models import Pages
import urllib.request

# Create your views here.
def lista(request):
    listado = Pages.objects.all()
    response = "Contenido del diccionario:\n<ul>"
    for recurso in listado:
        response += "<li>" + recurso.name + "</a>"
    return HttpResponse(response)
