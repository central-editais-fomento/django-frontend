# -*- coding: utf-8 -*
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Editais(models.Model):
	titulo	    = models.CharField(max_length=200)
	resumo	    = models.CharField(max_length=1000)
	texto	    = models.TextField()
	data_limite	= models.DateField()
	#TODO Futuramente areas e tipos devem ser transformados em modelos separados
	# areas são as grandes areas do CNPQ
	areas   = models.CharField(max_length=1000)
	# tipos são os tipos de itens financiáveis: bolsas, eventos ou outros
	tipos   = models.CharField(max_length=1000)