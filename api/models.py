from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class StudentsData(models.Model):
    name = models.CharField(max_length=30, unique=True,blank=False, error_messages={
        "max_length":"maximo numero de caracteres 30",
        "unique":"Este nombre ya esta registrado",
        "blank":"no puede estar en blanco",
    })
    age = models.IntegerField(blank=False,validators=[
        MinValueValidator(0),
        MaxValueValidator(99),
    ], error_messages={
        "black":"No puede estar en blanco",
    })
    yearstudent = models.CharField(max_length=5, blank=False, error_messages={
        "max_length":"No puede Tener mas de 5 caracteres",
        "blank":"No puede estar en Blanco",
    })
    dni = models.CharField(max_length=20, blank=True, unique=True, error_messages={
        "max_length":"No puede tener mas de 20 caracteres",
        "blank":"Puede estar en blanco",
        "unique":"Esta Cedula ya esta registrada, Verifique los Datos Ingresados",
    })
    family = models.CharField(max_length=100, blank=False, error_messages={
        "max_length":"No puede tener mas de 100 caracteres",
        "blank":"No puede Estar en Blanco",
    })
    phone = models.CharField(max_length=40, blank=False, error_messages={
        "max_length":"No puede Tener mas de 40 caracteres",
        "blank":"No puede estar en Blanco el numero de Telefono",
    })
    note = models.CharField(blank=True)

class TeachersData(models.Model):
    name = models.CharField(max_length=50, blank=False, error_messages={
        "max_length":"No se puede tener mas de 40 caracteres",
        "blank":"no se puede dejar en blanco",
    })
    age = models.IntegerField(blank=False,validators=[
        MinValueValidator(0),
        MaxValueValidator(99),
    ], error_messages={
        "blank":"no pueden estar en blanco",
    })
    dni = models.CharField(max_length=20, blank=False, unique=True, error_messages={
        "max_length":"No puede tener mas de 20 caracteres",
        "blank":"No Puede estar en blanco",
        "unique":"Esta Cedula ya esta registrada, Verifique los Datos Ingresados",
    })

    yearstudentasign = models.CharField(max_length=10,null=True, blank=False, error_messages={
        "max_length":"no puede tener mas de 10",
        "blank":"No puede estar en blanco",
    })
    phone = models.CharField(max_length=40, blank=False, error_messages={
        "max_length":"No puede Tener mas de 40 caracteres",
        "blank":"No puede estar en Blanco el numero de Telefono",
    })
    note = models.CharField(blank=True, max_length=255, error_messages={
        "max_length":"no pude contener mas de 255 caracteres",
    })

