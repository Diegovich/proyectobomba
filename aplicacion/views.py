from django.shortcuts import redirect, render
from django.contrib import messages
from django.views.decorators.cache import never_cache

from aplicacion.forms import formularioCargaCamioneta
from aplicacion.models import CargaCamioneta


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

def listaCargaCamioneta(request):
    car = CargaCamioneta.objects.all()
    data = {
        'cargasCamioneta' : car
    }
    return render(request,'bombero/cargaCamioneta.html', data )

def editarCargaCamioneta(request, id):
    cargas = CargaCamioneta.objects.get(id=id)
    formulario = formularioCargaCamioneta(instance=cargas)
    if request.method == 'POST':
        formulario = formularioCargaCamioneta(request.POST, instance=cargas)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Carga editada con exito !')
    data = {
        'titulo': 'Editar Carga a Camioneta',
        'formulario' : formulario,
        'ruta' : '/cargacamioneta'
    }
    return render(request, 'create.html', data)

def eliminarCargaCamioneta(request,id):
    carga = CargaCamioneta.objects.get(id=id)
    carga.delete()
    return redirect('/cargacamioneta')