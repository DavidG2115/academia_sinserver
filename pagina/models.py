from typing import Any, Dict, Tuple
from django.db import models

# Create your models here.
class Curso(models.Model):
    
    imagen = models.ImageField(upload_to='images/', null=True)
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(null=True)
    consultor = models.CharField(max_length=100, null=True)
    aprenderas = models.TextField(null=True)


    def __str__(self):
     return self.nombre
    def delete(self, using:None, keep_parents:False):
        self.image.storage.delete(self.image.nombre)
        super().delete()

class Tema(models.Model): 
    
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    project = models.ForeignKey(Curso, on_delete=models.CASCADE)
    def __str__(self):
     return self.titulo