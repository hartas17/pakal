from django.db import models

# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField(max_length=256)

    def __str__(self):
        return f"{self.id}: {self.nombre}"
    
class Huerto(models.Model):
    nombre = models.CharField(max_length=256)
    direccion = models.CharField(max_length=256)
    propietario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="huertos")
    info = models.CharField(max_length=256)
    header_img = models.CharField(max_length=256, blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} | direccion: {self.direccion} | propietario: {self.propietario} | info: {self.info}"

class Foto(models.Model):
    url = models.CharField(max_length=256)
    id_huerto = models.ForeignKey(Huerto, on_delete=models.CASCADE, related_name="fotos")

    def __str__(self):
        return f"{self.url} | id_huerto: {self.id_huerto}"

class Comentario(models.Model):
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="usuario")
    id_huerto = models.ForeignKey(Huerto, on_delete=models.CASCADE, related_name="huerto")
    contenido = models.CharField(max_length=256)