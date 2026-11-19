from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('moradores/', views.cadastro_morador, name='cadastro_morador'),
    path('entregas/', views.cadastro_entrega, name='cadastro_entrega'),
    path('entradas/', views.verificacao_entradas, name='verificacao_entradas'),
    path('funcionarios/', views.cadastro_funcionario, name='cadastro_funcionario'),
    path('ocorrencias/', views.registro_ocorrencias, name='registro_ocorrencias'),
]