# -*- coding: utf-8 -*
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the central editais fomento index.")

# Comentei essa parte pois estava dando erro
# from django.shortcuts import render
# from django.http import HttpResponse
# from djtools.utils import rtr, httprr
# from django.contrib.auth.decorators import login_required
# from models import Editais
# from django.shortcuts import get_object_or_404
# from datetime import datetime

# @rtr()
# def index(request):
# 	editais = Editais.objects.all()
# 	return locals()
# #		return HttpResponse(u'Olá mundo!')

# @rtr()
# def busca(request):
# 	return locals()


# @rtr()
# def edital(request, edital_pk):
# 	edital = get_object_or_404(Editais, id=edital_pk)
# 	return locals()