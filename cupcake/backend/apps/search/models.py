from django.db import models


class Person(models.Model):
    GENDER_CHOICES = [("F", "Femenino"), ("M", "Masculino")]
    document = models.CharField(
        "DNI", max_length=8, blank=True, null=True)
    first_surname = models.CharField(
        "Apellido Paterno", max_length=30, blank=True, null=True)
    last_surname = models.CharField(
        "Apellido Materno", max_length=30, blank=True, null=True)
    name = models.CharField("Nombres", max_length=120, blank=True, null=True)
    date_birth = models.DateField("Fecha de Nacimiento", null=True, blank=True)
    ubigeo = models.PositiveIntegerField("Ubigeo Code", max_length=6, blank=True, null=True)
    ubigeo_name = models.CharField(
        "Ubigeo Name", max_length=250, blank=True, null=True)
    address = models.CharField(
        "Dirección", max_length=250, blank=True, null=True)
    gender = models.CharField(choices=GENDER_CHOICES,
                              max_length=30, blank=True, null=True)
    status_civil = models.CharField(
        "Estado Civil", max_length=250, blank=True, null=True)
    mother_name = models.CharField(
        "Nombre Madre", max_length=250, blank=True, null=True)
    father_name = models.CharField(
        "Nombre Padre", max_length=250, blank=True, null=True)

    class Meta:
        verbose_name = 'Persona'
        verbose_name_plural = "Personas"

    def __str__(self):
        return 'Persona %s' %(self.id) 
