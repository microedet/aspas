from django.db import models

# Create your models here.


# Modelo de administradores lo dará de alta el superusuario
class Administrador(models.Model):
    fotoAdministrador = models.ImageField(upload_to='core', verbose_name="fotoAdministrador")
    dniAdministrador = models.CharField(max_length=9)
    nombre = models.CharField(max_length=30)
    apellido1 = models.CharField(max_length=50)
    apellido2 = models.CharField(max_length=50)
    direccion = models.CharField(max_length=200)
    localidad = models.CharField(max_length=100)
    provincia = models.CharField(max_length=100)
    codigoPostal = models.IntegerField
    telefonoMovil = models.IntegerField
    telefonoFijo = models.IntegerField
    email = models.CharField(max_length=45)


    class Meta:
        verbose_name = "administrador"
        verbose_name_plural = 'administradores'

    def __str__(self):
        return str(self.idUsuario)+" "+self.dni + " " + self.nombre + " " + self.apellido


# Modelo de Empresa lo da de alta el administrador
class Empresa(models.Model):
    denominacionSocial = models.CharField(max_length=200)
    direccion = models.CharField(max_length=200)
    localidad = models.CharField(max_length=100)
    provincia = models.CharField(max_length=100)
    codigoPostal = models.IntegerField
    telefono = models.IntegerField
    fax = models.IntegerField
    email = models.CharField(max_length=45)
    cif = models.CharField(max_length=45)
    actividad = models.CharField(max_length=100)
    idAdministrador =  models.OneToOneField(Administrador, on_delete=models.SET("sin administrador"), primary_key=True, related_name="EmpresaIdAdministrador")

    class Meta:
        verbose_name = "Empresa"
        verbose_name_plural = 'Empresas'

    def __str__(self):
        return str(self.denominacionSocial) + " " + self.direccion + " " + self.localidad + " " + self.provincia + " "+ self.codigoPostal+ " " + self.telefono + " " + self.fax +" "+ self.email+ " " + self.cif + " " + self.actividad

