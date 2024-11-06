from django.shortcuts import render, redirect
from .models import Formulario
from .forms import FormularioForm

def crear_inscripcion(request):
    if request.method == 'POST':
        form = FormularioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_inscripciones')
    else:
        form = FormularioForm()
    return render(request, 'APP/crear_inscripcion.html', {'form': form})

def listar_inscripciones(request):
    formularios = Formulario.objects.all()
    return render(request, 'APP/listar_inscripciones.html', {'formularios': formularios})

def crear_inscripcion(request):
    if request.method == 'POST':
        form = FormularioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_inscripciones')
    else:
        form = FormularioForm()
    return render(request, 'APP/crear_inscripcion.html', {'form': form})

def modificar_inscripcion(request, id):
    inscripcion = Formulario.objects.get(id=id) 
    if request.method == 'POST':
        form = FormularioForm(request.POST, instance=inscripcion)
        if form.is_valid():
            form.save()
            return redirect('listar_inscripciones')
    else:
        form = FormularioForm(instance=inscripcion)
    return render(request, 'APP/crear_inscripcion.html', {'form': form})

def eliminar_inscripcion(request, id):
    inscripcion = Formulario.objects.get(id=id)  
    inscripcion.delete()
    return redirect('listar_inscripciones')
