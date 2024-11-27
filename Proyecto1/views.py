import requests
from django.shortcuts import render, get_object_or_404
from .models import Servicio, Proyecto, Consulta
from .forms import ServicioForm, ProyectoForm, ConsultaForm, BusquedaForm, TestimonioForm
from django.http import JsonResponse
from django.shortcuts import redirect

def home(request):
    return render(request, 'home.html')

def servicios(request):
    servicios = Servicio.objects.all()
    return render(request, 'servicios.html', {'servicios': servicios})

def proyectos(request):
    proyectos = Proyecto.objects.all()
    return render(request, 'proyectos.html', {'proyectos': proyectos})

def contacto(request):
    if request.method == 'POST':
        form = ConsultaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ConsultaForm()
    return render(request, 'contacto.html', {'form': form})

def detalle_servicio(request, id):
    servicio = get_object_or_404(Servicio, id=id)
    testimonios = servicio.testimonios.all()

    if request.method == 'POST':
        form = TestimonioForm(request.POST)
        if form.is_valid():
            # Asocia el testimonio al servicio
            testimonio = form.save(commit=False)
            testimonio.servicio = servicio
            testimonio.save()
            # Redirigir a la misma página para mostrar el testimonio recién guardado
            return redirect('detalle_servicio', id=id)
    else:
        form = TestimonioForm()

    return render(request, 'detalle_servicio.html', {
        'servicio': servicio,
        'testimonios': testimonios,
        'form': form,
    })

def detalle_proyecto(request, id):
    proyecto = get_object_or_404(Proyecto, id=id)
    return render(request, 'detalle_proyecto.html', {'proyecto': proyecto})

def buscar(request):
    form = BusquedaForm()
    query = request.GET.get('query')
    resultados = []
    if query:
        servicios = Servicio.objects.filter(nombre__icontains=query)
        proyectos = Proyecto.objects.filter(titulo__icontains=query)
        for servicio in servicios:
            resultados.append({'tipo': 'servicio', 'objeto': servicio})
        for proyecto in proyectos:
            resultados.append({'tipo': 'proyecto', 'objeto': proyecto})
    return render(request, 'buscar.html', {'form': form, 'resultados': resultados})
