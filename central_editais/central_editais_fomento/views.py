#from django.http import HttpResponse
#from django.template import loader
from django.shortcuts import render
from .models import Edital

def index(request):
    #TODO listar por padrão somente os editais abertos
	editais = Edital.objects.all()
	context = {'editais': editais}
	return render(request, 'central_editais_fomento/index.html', context)

def todos(request):
	editais = Edital.objects.all()
	context = {'editais': editais}
	return render(request, 'central_editais_fomento/todos.html', context)

def busca(request):
	return HttpResponse("Página de busca")

def edital(request, edital_id):
	return HttpResponse("Página que mostra o edital %s" % edital_id)
