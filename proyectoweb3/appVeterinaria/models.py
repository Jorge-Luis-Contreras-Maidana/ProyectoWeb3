from django.db import models

class Dueno(models.Model):
    id_dueno = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    ci = models.CharField(max_length=20)
    telefono = models.CharField(max_length=20)
    direccion = models.CharField(max_length=150)
    email = models.EmailField(max_length=100)

    def __str__(self):

       return f"{self.nombre} - CI: {self.ci} | Tlf: {self.telefono} | Dir: {self.direccion} | Email: {self.email}"
    
    class Meta:
        managed = False
        db_table = 'duenos'

class Mascota(models.Model):
    id_mascota = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    especie = models.CharField(max_length=30)
    raza = models.CharField(max_length=50)
    sexo_choices = [
        ('Macho', 'Macho'),
        ('Hembra', 'Hembra'),
    ]
    sexo = models.CharField(max_length=6, choices=sexo_choices)
    fecha_nacimiento = models.DateField()
    id_dueno = models.ForeignKey('Dueno', models.DO_NOTHING, db_column='id_dueno')

    def __str__(self):
        return f"{self.nombre} - Especie: {self.especie} | Raza: {self.raza} | Sexo: {self.sexo} | Nacimiento: {self.fecha_nacimiento} | Dueño: {self.id_dueno.nombre}"
    
    class Meta:
        managed = False
        db_table = 'mascotas'

class Veterinario(models.Model):
    id_veterinario = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    matricula = models.CharField(max_length=20)
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return f"Dr(a). {self.nombre} - Matrícula: {self.matricula}"

    class Meta:
        managed = False
        db_table = 'veterinarios'

class Vacuna(models.Model):
    id_vacuna = models.AutoField(primary_key=True)
    nombre_vacuna = models.CharField(max_length=100)
    descripcion = models.TextField()
    dosis_requeridas = models.SmallIntegerField()
    intervalo_dias = models.SmallIntegerField()

    def __str__(self):
        return f"{self.nombre_vacuna} ({self.dosis_requeridas} dosis)"

    class Meta:
        managed = False
        db_table = 'vacunas'

class Cita(models.Model):
    id_cita = models.AutoField(primary_key=True)
    fecha = models.DateTimeField()
    motivo = models.CharField(max_length=100)
    
    # Relaciones de clave foránea
    id_mascota = models.ForeignKey(Mascota, models.DO_NOTHING, db_column='id_mascota')
    id_veterinario = models.ForeignKey(Veterinario, models.DO_NOTHING, db_column='id_veterinario')
    
    # Campo Enum para estado
    estado_choices = [
        ('Pendiente', 'Pendiente'),
        ('Atendida', 'Atendida'),
        ('Cancelada', 'Cancelada'),
    ]
    estado = models.CharField(max_length=10, choices=estado_choices)

    def __str__(self):
        return f"Cita {self.id_cita} - {self.id_mascota} - {self.fecha.strftime('%Y-%m-%d %H:%M')}"

    class Meta:
        managed = False
        db_table = 'citas'

class HistorialVacunacion(models.Model):
    id_vacunacion = models.AutoField(primary_key=True)
    dosis_numero = models.SmallIntegerField()
    fecha_aplicacion = models.DateField()
    fecha_proxima = models.DateField()
    observaciones = models.TextField()

    # Relaciones de clave foránea
    id_mascota = models.ForeignKey(Mascota, models.DO_NOTHING, db_column='id_mascota')
    id_vacuna = models.ForeignKey(Vacuna, models.DO_NOTHING, db_column='id_vacuna')
    id_veterinario = models.ForeignKey(Veterinario, models.DO_NOTHING, db_column='id_veterinario')

    def __str__(self):
        return f"Vacuna {self.id_vacuna.nombre_vacuna} (Dosis {self.dosis_numero}) aplicada a {self.id_mascota.nombre} el {self.fecha_aplicacion}"

    class Meta:
        managed = False
        db_table = 'historial_vacunacion'
