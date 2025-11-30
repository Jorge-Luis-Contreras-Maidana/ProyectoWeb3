from django.contrib import admin
from .models import Cita, Dueno, HistorialVacunacion, Mascota, Vacuna, Veterinario

# Register your models here.
# --- DUEÑOS ---
@admin.register(Dueno)
class DuenoAdmin(admin.ModelAdmin):
    list_display = ('id_dueno', 'nombre', 'ci', 'telefono', 'direccion', 'email')
    search_fields = ('nombre', 'ci', 'telefono')


# --- MASCOTAS ---
@admin.register(Mascota)
class MascotaAdmin(admin.ModelAdmin):
    list_display = ('id_mascota', 'nombre', 'especie', 'raza', 'sexo', 'fecha_nacimiento', 'id_dueno')
    list_filter = ('especie', 'sexo')
    search_fields = ('nombre', 'raza')


# --- VETERINARIOS ---
@admin.register(Veterinario)
class VeterinarioAdmin(admin.ModelAdmin):
    list_display = ('id_veterinario', 'nombre', 'matricula', 'telefono')
    search_fields = ('nombre', 'matricula')


# --- VACUNAS ---
@admin.register(Vacuna)
class VacunaAdmin(admin.ModelAdmin):
    list_display = ('id_vacuna', 'nombre_vacuna', 'descripcion', 'dosis_requeridas', 'intervalo_dias')
    search_fields = ('nombre_vacuna',)


# --- CITAS ---
@admin.register(Cita)
class CitaAdmin(admin.ModelAdmin):
    list_display = ('id_cita', 'fecha', 'motivo', 'id_mascota', 'id_veterinario', 'estado')
    list_filter = ('estado', 'fecha')
    search_fields = ('motivo',)


# --- HISTORIAL VACUNACIÓN ---
@admin.register(HistorialVacunacion)
class HistorialVacunacionAdmin(admin.ModelAdmin):
    list_display = (
        'id_vacunacion',
        'id_mascota',
        'id_vacuna',
        'id_veterinario',
        'dosis_numero',
        'fecha_aplicacion',
        'fecha_proxima'
    )
    list_filter = ('fecha_aplicacion', 'fecha_proxima')