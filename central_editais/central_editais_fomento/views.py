# -*- coding: utf-8 -*
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from models import Editais
from django.shortcuts import get_object_or_404
from datetime import datetime

def index(request):
	editais = Editais.objects.all()
	context = {'editais': editais}
	return render(request, 'index.html', context)

# Comentei essa parte pois estava dando erro

# @rtr()
#def index(request):
#	editais = Editais.objects.all()
# 	return locals()
# #		return HttpResponse(u'Olá mundo!')

# @rtr()
#def busca(request):
#	return locals()


# @rtr()
#def edital(request, edital_pk):
#	edital = get_object_or_404(Editais, id=edital_pk)
#	context = {'edital': edital}
#	return render(request, 'edital.html', context)
#	return locals()