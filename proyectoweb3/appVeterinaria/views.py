from django.shortcuts import render, redirect, get_object_or_404
from .models import Dueno, Mascota, Veterinario, Vacuna, Cita, HistorialVacunacion 
from .forms import duenoForm, mascotaForm, veterinarioForm, vacunaForm, citaForm, historialvacunacionForm
from django.contrib.auth.decorators import login_required
from datetime import date
# Create your views here.

@login_required # Solo usuarios logueados pueden acceder
def principal_veterinaria(request):
    """Muestra la página de inicio/información después del login."""
    return render(request, 'principal_veterinaria.html', {})

def listar_duenos(request):
    duenos = Dueno.objects.all() # igual al SELECT * FROM Clientes
    return render(request, 'listar_duenos.html',{'duenos': duenos})

def eliminar_dueno(request, id):
    dueno = get_object_or_404(Dueno, id_dueno = id)
    dueno.delete()
    return redirect('listar_duenos')

def actualizar_dueno(request, id):
    dueno = get_object_or_404(Dueno, id_dueno = id)
    if request.method == 'POST':
        form = duenoForm(request.POST)
        if form.is_valid():

            dueno.nombre = form.cleaned_data['nombre']
            dueno.ci = form.cleaned_data['ci']
            dueno.telefono = form.cleaned_data['telefono']
            dueno.direccion = form.cleaned_data['direccion']
            dueno.email = form.cleaned_data['correo']
            dueno.save()
            return redirect('listar_duenos')
    else:
        form = duenoForm(initial={
            'nombre': dueno.nombre,
            'ci': dueno.ci,
            'telefono': dueno.telefono,
            'direccion': dueno.direccion,
            'correo': dueno.email,
        })
    return render(request, 'actualizar_dueno.html', {'form': form})

def crear_dueno(request):
    if request.method == 'POST':
        form = duenoForm(request.POST)
        if  form.is_valid():
            Dueno.objects.create(
                nombre = form.cleaned_data['nombre'],
                ci = form.cleaned_data['ci'],
                telefono = form.cleaned_data['telefono'],
                direccion = form.cleaned_data['direccion'],
                email = form.cleaned_data['correo']
            )
            return redirect('listar_duenos')
    else:
        form = duenoForm()
        return render(request, 'nuevo_dueno.html',{'form': form})

# =================================================================================================
def listar_mascotas(request):
    mascotas = Mascota.objects.all()
    return render(request, 'listar_mascotas.html', {'mascotas': mascotas})

def eliminar_mascota(request, id):
    mascota = get_object_or_404(Mascota, id_mascota = id)
    mascota.delete()
    return redirect('listar_mascotas')

def actualizar_mascota(request, id):
    mascota = get_object_or_404(Mascota, id_mascota = id)
    if request.method == 'POST':
        form = mascotaForm(request.POST)
        if form.is_valid():
            
            mascota.nombre = form.cleaned_data['nombre']
            mascota.especie = form.cleaned_data['especie']
            mascota.raza = form.cleaned_data['raza']
            mascota.sexo = form.cleaned_data['sexo']
            mascota.fecha_nacimiento = form.cleaned_data['fecha_nacimiento']
            mascota.id_dueno = form.cleaned_data['id_dueno'] 
            
            mascota.save()
            return redirect('listar_mascotas')
    else:
        form = mascotaForm(initial={
            'nombre': mascota.nombre,
            'especie': mascota.especie,
            'raza': mascota.raza,
            'sexo': mascota.sexo,
            'fecha_nacimiento': mascota.fecha_nacimiento,
            'id_dueno': mascota.id_dueno,
        })
    return render(request, 'actualizar_mascota.html', {'form': form})

def crear_mascota(request):
    if request.method == 'POST':
        form = mascotaForm(request.POST)
        if form.is_valid():
            Mascota.objects.create(
                nombre = form.cleaned_data['nombre'],
                especie = form.cleaned_data['especie'],
                raza = form.cleaned_data['raza'],
                sexo = form.cleaned_data['sexo'],
                fecha_nacimiento = form.cleaned_data['fecha_nacimiento'],
                id_dueno = form.cleaned_data['id_dueno']
            )
            return redirect('listar_mascotas')
    else:
        form = mascotaForm()
        return render(request, 'nueva_mascota.html', {'form': form})
    
# =============================================================================

def listar_veterinarios(request):
    veterinarios = Veterinario.objects.all()
    return render(request, 'listar_veterinarios.html', {'veterinarios': veterinarios})

def eliminar_veterinario(request, id):
    veterinario = get_object_or_404(Veterinario, id_veterinario = id)
    veterinario.delete()
    return redirect('listar_veterinarios')

def actualizar_veterinario(request, id):
    veterinario = get_object_or_404(Veterinario, id_veterinario = id)
    if request.method == 'POST':
        form = veterinarioForm(request.POST)
        if form.is_valid():
            
            veterinario.nombre = form.cleaned_data['nombre']
            veterinario.matricula = form.cleaned_data['matricula']
            veterinario.telefono = form.cleaned_data['telefono']
            
            veterinario.save()
            return redirect('listar_veterinarios')
    else:
        form = veterinarioForm(initial={
            'nombre': veterinario.nombre,
            'matricula': veterinario.matricula,
            'telefono': veterinario.telefono,
        })
    return render(request, 'actualizar_veterinario.html', {'form': form})

def crear_veterinario(request):
    if request.method == 'POST':
        form = veterinarioForm(request.POST)
        if form.is_valid():
            Veterinario.objects.create(
                nombre = form.cleaned_data['nombre'],
                matricula = form.cleaned_data['matricula'],
                telefono = form.cleaned_data['telefono']
            )
            return redirect('listar_veterinarios')
    else:
        form = veterinarioForm()
        return render(request, 'nuevo_veterinario.html', {'form': form})
    

# ======================================================================

def listar_vacunas(request):
    vacunas = Vacuna.objects.all()
    return render(request, 'listar_vacunas.html', {'vacunas': vacunas})

def eliminar_vacuna(request, id):
    vacuna = get_object_or_404(Vacuna, id_vacuna = id)
    vacuna.delete()
    return redirect('listar_vacunas')

def actualizar_vacuna(request, id):
    vacuna = get_object_or_404(Vacuna, id_vacuna = id)
    if request.method == 'POST':
        form = vacunaForm(request.POST)
        if form.is_valid():
            
            vacuna.nombre_vacuna = form.cleaned_data['nombre_vacuna']
            vacuna.descripcion = form.cleaned_data['descripcion']
            vacuna.dosis_requeridas = form.cleaned_data['dosis_requeridas']
            vacuna.intervalo_dias = form.cleaned_data['intervalo_dias']
            
            vacuna.save()
            return redirect('listar_vacunas')
    else:
        form = vacunaForm(initial={
            'nombre_vacuna': vacuna.nombre_vacuna,
            'descripcion': vacuna.descripcion,
            'dosis_requeridas': vacuna.dosis_requeridas,
            'intervalo_dias': vacuna.intervalo_dias,
        })
    return render(request, 'actualizar_vacuna.html', {'form': form})

def crear_vacuna(request):
    if request.method == 'POST':
        form = vacunaForm(request.POST)
        if form.is_valid():
            Vacuna.objects.create(
                nombre_vacuna = form.cleaned_data['nombre_vacuna'],
                descripcion = form.cleaned_data['descripcion'],
                dosis_requeridas = form.cleaned_data['dosis_requeridas'],
                intervalo_dias = form.cleaned_data['intervalo_dias']
            )
            return redirect('listar_vacunas')
    else:
        form = vacunaForm()
        return render(request, 'nueva_vacuna.html', {'form': form})
    

# =====================================================================================

def listar_citas(request):
    from datetime import datetime
    mostrar_futuras = request.GET.get('futuras', None)
    
    if mostrar_futuras:
        # Usar datetime para comparar con DateTimeField
        ahora = datetime.now()
        citas = Cita.objects.filter(fecha__gte=ahora).order_by('fecha')
    else:
        citas = Cita.objects.all().order_by('fecha')
    
    return render(request, 'listar_citas.html', {
        'citas': citas,
        'mostrar_futuras': mostrar_futuras
    })

def eliminar_cita(request, id):
    cita = get_object_or_404(Cita, id_cita = id)
    cita.delete()
    return redirect('listar_citas')

def actualizar_cita(request, id):
    cita = get_object_or_404(Cita, id_cita = id)
    if request.method == 'POST':
        form = citaForm(request.POST)
        if form.is_valid():
            
            cita.fecha = form.cleaned_data['fecha']
            cita.motivo = form.cleaned_data['motivo']
            cita.id_mascota = form.cleaned_data['id_mascota']
            cita.id_veterinario = form.cleaned_data['id_veterinario']
            cita.estado = form.cleaned_data['estado']
            
            cita.save()
            return redirect('listar_citas')
    else:
        form = citaForm(initial={
            'fecha': cita.fecha,
            'motivo': cita.motivo,
            'id_mascota': cita.id_mascota,
            'id_veterinario': cita.id_veterinario,
            'estado': cita.estado,
        })
    return render(request, 'actualizar_cita.html', {'form': form})

def crear_cita(request):
    if request.method == 'POST':
        form = citaForm(request.POST)
        if form.is_valid():
            Cita.objects.create(
                fecha = form.cleaned_data['fecha'],
                motivo = form.cleaned_data['motivo'],
                id_mascota = form.cleaned_data['id_mascota'],
                id_veterinario = form.cleaned_data['id_veterinario'],
                estado = form.cleaned_data['estado']
            )
            return redirect('listar_citas')
    else:
        form = citaForm()
        return render(request, 'nueva_cita.html', {'form': form})
    

#=======================================================================

def listar_historial(request):
    historiales = HistorialVacunacion.objects.all()
    return render(request, 'listar_historial.html', {'historiales': historiales})

def eliminar_historial(request, id):
    historial = get_object_or_404(HistorialVacunacion, id_vacunacion = id)
    historial.delete()
    return redirect('listar_historial')

def actualizar_historial(request, id):
    historial = get_object_or_404(HistorialVacunacion, id_vacunacion = id)
    if request.method == 'POST':
        form = historialvacunacionForm(request.POST)
        if form.is_valid():
            
            historial.dosis_numero = form.cleaned_data['dosis_numero']
            historial.fecha_aplicacion = form.cleaned_data['fecha_aplicacion']
            historial.fecha_proxima = form.cleaned_data['fecha_proxima']
            historial.observaciones = form.cleaned_data['observaciones']
            historial.id_mascota = form.cleaned_data['id_mascota']
            historial.id_vacuna = form.cleaned_data['id_vacuna']
            historial.id_veterinario = form.cleaned_data['id_veterinario']
            
            historial.save()
            return redirect('listar_historial')
    else:
        form = historialvacunacionForm(initial={
            'dosis_numero': historial.dosis_numero,
            'fecha_aplicacion': historial.fecha_aplicacion,
            'fecha_proxima': historial.fecha_proxima,
            'observaciones': historial.observaciones,
            'id_mascota': historial.id_mascota,
            'id_vacuna': historial.id_vacuna,
            'id_veterinario': historial.id_veterinario,
        })
    return render(request, 'actualizar_historial.html', {'form': form})

def crear_historial(request):
    if request.method == 'POST':
        form = historialvacunacionForm(request.POST)
        if form.is_valid():
            HistorialVacunacion.objects.create(
                dosis_numero = form.cleaned_data['dosis_numero'],
                fecha_aplicacion = form.cleaned_data['fecha_aplicacion'],
                fecha_proxima = form.cleaned_data['fecha_proxima'],
                observaciones = form.cleaned_data['observaciones'],
                id_mascota = form.cleaned_data['id_mascota'],
                id_vacuna = form.cleaned_data['id_vacuna'],
                id_veterinario = form.cleaned_data['id_veterinario']
            )
            return redirect('listar_historial')
    else:
        form = historialvacunacionForm()
        return render(request, 'nuevo_historial.html', {'form': form})
    

# ======================================================
def calendario_vacunas(request):
    from datetime import timedelta
    # Obtener parámetro para filtrar solo próximas vacunas
    mostrar_proximas = request.GET.get('proximas', None)
    
    if mostrar_proximas:
        # Filtrar solo vacunas próximas (fecha_proxima >= hoy)
        vacunas = HistorialVacunacion.objects.filter(
            fecha_proxima__gte=date.today()
        ).order_by('fecha_proxima')
    else:
        # Mostrar todas las vacunas ordenadas por fecha próxima
        vacunas = HistorialVacunacion.objects.all().order_by('fecha_proxima')
    
    # Calcular fechas para comparación
    hoy = date.today()
    pronto = hoy + timedelta(days=7)  # Próximos 7 días
    
    return render(request, 'calendario_vacunas.html', {
        'vacunas': vacunas,
        'mostrar_proximas': mostrar_proximas,
        'today': hoy,
        'pronto': pronto
    })