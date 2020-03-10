from django.http import HttpResponse
from django.template import loader
from .models import Edital

def index(request):
	editais = Edital.objects.all()
	context = {'editais': editais}
	template = loader.get_template('central_editais_fomento/index.html')
	return HttpResponse(template.render(context,request))

def busca(request):
	return HttpResponse("Página de busca")

def edital(request, edital_id):
	return HttpResponse("Página que mostra o edital %s" % edital_id)