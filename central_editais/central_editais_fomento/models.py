from django.db import models

# Create your models here.
class Edital(models.Model):
	titulo	    = models.CharField(max_length=200)
	resumo	    = models.CharField(max_length=1000)
	texto	    = models.TextField()
	data_limite	= models.DateField()
	#TODO Futuramente talvez areas e tipos devam ser transformados em modelos separados
	# areas são as areas do CNPQ
	areas   = models.CharField(max_length=1000)
	# tipos são os tipos de itens financiáveis: bolsas, eventos ou outros
	tipos   = models.CharField(max_length=1000)

	def __str__(self):
		return self.titulo