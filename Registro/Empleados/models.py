from django.db import models

# Create your models here.

class Empleaos(models.Model):
    PrimerNombre = models.CharField(max_length=20)
    PrimerApellido = models.CharField(max_length=20)
    OtrosNombres = models.CharField(max_length=50)
    PaisEmpleo = models.CharField(max_length=15)
    Correo = models.CharField(max_length=300)
    