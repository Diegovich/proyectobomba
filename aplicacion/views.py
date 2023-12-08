from django.shortcuts import render
from django.contrib import messages
from django.views.decorators.cache import never_cache

from aplicacion.forms import formularioCargaCamioneta


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

def cargaBomba(request):
    context = {'nombrePagina': 'Carga Camioneta'}
    return render(request, 'bombero/cargaCamioneta.html', context)

def cargaCamioneta(request):
    formulario = formularioCargaCamioneta()
    if request.method == 'POST':
        formulario = formularioCargaCamioneta(request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'carga realizada con exito')
    data = {
        'titulo':'Carga de combustible a camioneta',
        'formulario':formulario,
        'ruta':'/cargaCamioneta'
    }
    return render (request,'create.html',data)