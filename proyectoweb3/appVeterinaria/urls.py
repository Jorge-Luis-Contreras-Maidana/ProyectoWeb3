from django.contrib import admin
from django.urls import path, include
from appVeterinaria import views


urlpatterns = [
    path('duenos/', views.listar_duenos, name='listar_duenos'),
    path('eliminar_dueno/<int:id>/', views.eliminar_dueno, name='eliminar_dueno'),
    path('actualizar_dueno/<int:id>/', views.actualizar_dueno, name='actualizar_dueno'),
    path('nuevo_dueno/', views.crear_dueno, name= 'crear_dueno'),
    # ==============================
    path('mascotas/', views.listar_mascotas, name='listar_mascotas'),
    path('nueva_mascota/', views.crear_mascota, name='crear_mascota'),
    path('eliminar_mascota/<int:id>/', views.eliminar_mascota, name='eliminar_mascota'),
    path('actualizar_mascota/<int:id>/', views.actualizar_mascota, name='actualizar_mascota'),
    # =========================================
    # 👨‍⚕️ Rutas para Veterinarios
    path('veterinarios/', views.listar_veterinarios, name='listar_veterinarios'),
    path('nuevo_veterinario/', views.crear_veterinario, name='crear_veterinario'),
    path('eliminar_veterinario/<int:id>/', views.eliminar_veterinario, name='eliminar_veterinario'),
    path('actualizar_veterinario/<int:id>/', views.actualizar_veterinario, name='actualizar_veterinario'),

    # 💉 Rutas para Vacunas
    path('vacunas/', views.listar_vacunas, name='listar_vacunas'),
    path('nueva_vacuna/', views.crear_vacuna, name='crear_vacuna'),
    path('eliminar_vacuna/<int:id>/', views.eliminar_vacuna, name='eliminar_vacuna'),
    path('actualizar_vacuna/<int:id>/', views.actualizar_vacuna, name='actualizar_vacuna'),

    # 📅 Rutas para Citas
    path('citas/', views.listar_citas, name='listar_citas'),
    path('nueva_cita/', views.crear_cita, name='crear_cita'),
    path('eliminar_cita/<int:id>/', views.eliminar_cita, name='eliminar_cita'),
    path('actualizar_cita/<int:id>/', views.actualizar_cita, name='actualizar_cita'),

    # 📜 Rutas para Historial de Vacunación
    path('historial/', views.listar_historial, name='listar_historial'),
    path('nuevo_historial/', views.crear_historial, name='crear_historial'),
    path('eliminar_historial/<int:id>/', views.eliminar_historial, name='eliminar_historial'),
    path('actualizar_historial/<int:id>/', views.actualizar_historial, name='actualizar_historial'),
    # 📅 Calendario de Vacunas
    path('calendario_vacunas/', views.calendario_vacunas, name='calendario_vacunas'),
]
