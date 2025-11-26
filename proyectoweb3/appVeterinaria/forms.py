from django import forms
from .models import Dueno, Mascota, Veterinario, Vacuna

class duenoForm(forms.Form):
    nombre = forms.CharField(label="Nombre", required=True)
    ci = forms.CharField(label="Ci", required=True)
    telefono = forms.CharField(label="Telefono", required=True)
    direccion = forms.CharField(label="Direccion", required=True)
    correo = forms.EmailField(label="Correo", required=True)

class mascotaForm(forms.Form):
    nombre = forms.CharField(label="Nombre", max_length=50, required=True)
    especie = forms.CharField(label="Especie", max_length=30, required=True)
    raza = forms.CharField(label="Raza", max_length=50, required=True)
    sexo_choices = [
        ('Macho', 'Macho'),
        ('Hembra', 'Hembra'),
    ]
    sexo = forms.ChoiceField(label="Sexo", choices=sexo_choices, required=True)
    
    fecha_nacimiento = forms.DateField(label="Fecha de Nacimiento", widget=forms.DateInput(attrs={'type': 'date'}),required=True)
    
    id_dueno = forms.ModelChoiceField(
        queryset=Dueno.objects.all(),
        label="Dueño",
        required=True
    )
class veterinarioForm(forms.Form):
    nombre = forms.CharField(label="Nombre", max_length=100, required=True)
    matricula = forms.CharField(label="Matrícula", max_length=20, required=True)
    telefono = forms.CharField(label="Telefono", max_length=20, required=True)

class vacunaForm(forms.Form):
    nombre_vacuna = forms.CharField(label="Nombre Vacuna", max_length=100, required=True)
    descripcion = forms.CharField(label="Descripción", widget=forms.Textarea, required=False)
    dosis_requeridas = forms.IntegerField(label="Dosis Requeridas", min_value=1, required=True)
    intervalo_dias = forms.IntegerField(label="Intervalo Días", min_value=1, required=True)

class citaForm(forms.Form):
    fecha = forms.DateTimeField(label="Fecha y Hora", widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}),required=True)
    motivo = forms.CharField(label="Motivo", max_length=100, required=True)
    
    # Campo 'estado' del modelo Cita
    estado_choices = [
        ('Pendiente', 'Pendiente'),
        ('Atendida', 'Atendida'),
        ('Cancelada', 'Cancelada'),
    ]
    estado = forms.ChoiceField(label="Estado", choices=estado_choices, required=True)
    
    # Claves Foráneas
    id_mascota = forms.ModelChoiceField(
        queryset=Mascota.objects.all(),
        label="Mascota",
        required=True
    )
    id_veterinario = forms.ModelChoiceField(
        queryset=Veterinario.objects.all(),
        label="Veterinario",
        required=True
    )

class historialvacunacionForm(forms.Form):
    dosis_numero = forms.IntegerField(label="Número de Dosis", min_value=1, required=True)
    fecha_aplicacion = forms.DateField(label="Fecha Aplicación", 
                                        widget=forms.DateInput(attrs={'type': 'date'}), 
                                        required=True)
    fecha_proxima = forms.DateField(label="Fecha Próxima", 
                                    widget=forms.DateInput(attrs={'type': 'date'}), 
                                    required=False) # Fecha futura puede ser opcional
    observaciones = forms.CharField(label="Observaciones", widget=forms.Textarea, required=False)
    
    # Claves Foráneas
    id_mascota = forms.ModelChoiceField(
        queryset=Mascota.objects.all(),
        label="Mascota",
        required=True
    )
    id_vacuna = forms.ModelChoiceField(
        queryset=Vacuna.objects.all(),
        label="Vacuna",
        required=True
    )
    id_veterinario = forms.ModelChoiceField(
        queryset=Veterinario.objects.all(),
        label="Veterinario",
        required=True
    )

