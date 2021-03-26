from django.db import models

# Create your models here.

from django.db import models

# Create your models here.

class Userbc21(models.Model):
    GENERO = (
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('O', 'Otro'),
    )
    #id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length = 50)
    email = models.CharField(max_length = 50)
    telefono = models.CharField(max_length = 20)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    genero = models.CharField(blank=True, null=True, max_length=1, choices=GENERO)
    entidad_organizacion = models.CharField(blank=True,null=True, max_length = 50)
    cargo = models.CharField(blank=True, null=True,max_length = 50)
    departamento = models.CharField(blank=True,null=True,max_length = 50)
    municipio = models.CharField(blank=True,null=True, max_length = 50)

    def __str__(self):
        return self.nombre