from django.shortcuts import render
from .models import *

# Create your views here.

def funcionarios(request):
    funcionarios = {
        'funcionarios': Funcionario.objects.all()
    }
    return render(request, 'funcionarios.html', funcionarios)

def departamentos(request):
    departamentos = {
        'departamentos': Departamento.objects.all()
    }
    return render(request, 'departamentos.html', departamentos)

def projetos(request):
    projetos = {
        'projetos': Projeto.objects.all()
    }
    return render(request, 'projetos.html', projetos)

def beneficios(request):
    beneficios = {
        'beneficios': Beneficio.objects.all()
    }
    return render(request, 'beneficios.html', beneficios)