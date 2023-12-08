from django.shortcuts import render
from django.views.decorators.cache import never_cache


@never_cache

def inicio(request):
    return render(request,'base.html')

def registro(request):
    context = {'nombrePagina': 'Registro de Usuarios'}
    return render(request, 'administrador/registrousuarios.html', context)

def informes(request):
    context = {'nombrePagina': 'Informes'}
    return render(request, 'administrador/informes.html', context)

def iniciarJornada(request):
    context = {'nombrePagina': 'Iniciar Jornada Laboral'}
    return render(request, 'bombero/iniciarJornada.html', context)

def cargaCamioneta(request):
    context = {'nombrePagina': 'Carga Camioneta'}
    return render(request, 'bombero/cargaCamioneta.html', context)

def cargaBomba(request):
    context = {'nombrePagina': 'Carga de Bomba'}
    return render(request, 'bombero/cargaBomba.html', context)
