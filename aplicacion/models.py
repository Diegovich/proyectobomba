from django.db import models
from django.core.exceptions import ValidationError

def validate_rut(value):
    # validacion
    pass

class Persona(models.Model):
    rut = models.CharField(max_length=12, primary_key=True, validators=[validate_rut])
    nombre = models.CharField(max_length=100)
    # fechaNacimiento = models.DateField()

    class Meta:
        abstract = True

class Administrador(Persona):
    pass

class Bombero(Persona):
    pass

class Camioneta(models.Model):
    patente = models.CharField(max_length=6)
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    ano = models.PositiveIntegerField()

class Chofer(Persona):
    camioneta = models.OneToOneField(Camioneta, on_delete=models.RESTRICT)

class Bomba(models.Model):
    capacidad = models.PositiveIntegerField(default=2000)
    litrosActuales = models.PositiveIntegerField()

    def esta_bajo_combustible(self):
        return self.litrosActuales < 150

class CargaBomba(models.Model):
    bomba = models.ForeignKey(Bomba, on_delete=models.RESTRICT)
    bombero = models.ForeignKey(Bombero, on_delete=models.RESTRICT)
    fechaCarga = models.DateTimeField(auto_now_add=True)
    litrosCargados = models.PositiveIntegerField()

class CargaCamioneta(models.Model):
    chofer = models.ForeignKey(Chofer, on_delete=models.RESTRICT)
    bomba = models.ForeignKey(Bomba, on_delete=models.RESTRICT)
    fechaCarga = models.DateTimeField(auto_now_add=True)
    litrosCargados = models.PositiveIntegerField()
    kilometrajeActual = models.PositiveIntegerField()
