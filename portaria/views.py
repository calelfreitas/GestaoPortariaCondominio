from django.shortcuts import render, redirect
from .models import Morador, Funcionario, Entrega, Entrada, Ocorrencia
from .forms import MoradorForm, FuncionarioForm, EntregaForm, EntradaForm, OcorrenciaForm

def index(request):
    contexto = {
        'total_moradores': Morador.objects.count(),
        'entregas_pendentes': Entrega.objects.filter(retirado=False).count(),
        'entradas_recentes': Entrada.objects.order_by('-data_hora_entrada')[:5],
        'ocorrencias_recentes': Ocorrencia.objects.order_by('-data_registro')[:5],
    }
    return render(request, 'portaria/index.html', contexto)

def cadastro_morador(request):
    form = MoradorForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('cadastro_morador')
    moradores = Morador.objects.all()
    return render(request, 'portaria/moradores.html', {'form': form, 'moradores': moradores})

def cadastro_entrega(request):
    form = EntregaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('cadastro_entrega')
    entregas = Entrega.objects.order_by('-data_recebimento')
    return render(request, 'portaria/entregas.html', {'form': form, 'entregas': entregas})

def verificacao_entradas(request):
    form = EntradaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('verificacao_entradas')
    entradas = Entrada.objects.order_by('-data_hora_entrada')
    return render(request, 'portaria/entradas.html', {'form': form, 'entradas': entradas})

def cadastro_funcionario(request):
    form = FuncionarioForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('cadastro_funcionario')
    funcionarios = Funcionario.objects.all()
    return render(request, 'portaria/funcionarios.html', {'form': form, 'funcionarios': funcionarios})

def registro_ocorrencias(request):
    form = OcorrenciaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('registro_ocorrencias')
    ocorrencias = Ocorrencia.objects.order_by('-data_registro')
    return render(request, 'portaria/ocorrencias.html', {'form': form, 'ocorrencias': ocorrencias})