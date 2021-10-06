from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models her

# Modelo para crear Personas
class Usuario(AbstractUser):
    foto = models.ImageField(upload_to='core', verbose_name="fotoUsuario")
    dni = models.CharField(max_length=9)
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
        verbose_name = "usuario"
        verbose_name_plural = 'usuarios'
        ordering = ['id']

    def __str__(self):
        return  self.dni + " " + self.nombre + " " + self.apellido


# Modelo de administradores lo dará de alta el superusuario
class Administrador(models.Model):
    idUsuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, primary_key=True,
                                     related_name="AdministradoridUsuario")

    class Meta:
        verbose_name = "administrador"
        verbose_name_plural = 'administradores'
        ordering = ['idUsuario']

    def __str__(self):
        return str(self.idUsuario)+" "+self.Usuario.dni+" "+self.Usuario.nombre+" "+self.Usuario.apellido1+" "+self.Usuario.apellido2+" "


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
        return str(self.denominacionSocial) + " "+str(self.idAdministrador) + " "+ self.direccion + " " + self.localidad + " " + self.provincia + " "+ self.codigoPostal+ " " + self.telefono + " " + self.fax +" "+ self.email+ " " + self.cif + " " + self.actividad


# Modelo de Cliente
class Cliente(models.Model):
    idUsuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, primary_key=True,
                                     related_name="ClienteidUsuario")

    class Meta:
        verbose_name = "cliente"
        verbose_name_plural = 'clientes'
        ordering = ['idUsuario']

    def __str__(self):
        return str(
            self.idUsuario) + " " + self.Usuario.dni + " " + self.Usuario.nombre + " " + self.Usuario.apellido1 + " " + self.Usuario.apellido2 + " "

# Modelo de empleado
class Empleado(models.Model):
    idUsuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, primary_key=True,
                                     related_name="EmpleadoidUsuario")
    idEmpresa = models.ForeignKey(Empresa, on_delete=models.SET_NULL, related_name="EmpleadoidEmpresa")

    class Meta:
        verbose_name = "empleado"
        verbose_name_plural = 'empleados'
        ordering = ['idUsuario']

    def __str__(self):
        return str(
            self.idUsuario) + " " + self.idEmpresa.denominacionSocial + " " + self.Usuario.nombre + " " + self.Usuario.apellido1 + " " + self.Usuario.apellido2 + " "



