from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:edital_id>/', views.edital),
    path('busca/', views.busca),
]