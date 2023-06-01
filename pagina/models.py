from typing import Any, Dict, Tuple
from django.db import models
from embed_video.fields import EmbedVideoField
import os

# Create your models here.

    
class Mentore(models.Model):
    nombre = models.CharField(max_length=100, null=True)
    imgconsultor = models.ImageField(upload_to='media', null=True)
    descripcion_breve = models.TextField(null=True)
    descripcion_amplia = models.TextField(null=True)
    
    def __str__(self):
      return self.nombre
    
    def delete(self, *args,**kwargs):
         if os.path.isfile(self.imgconsultor.path):
             os.remove(self.imgconsultor.path)
         super(Curso, self).delete(*args, **kwargs)
         
         
class Curso(models.Model):
    titulo = models.CharField(max_length=200)
    descipcion = models.TextField()
    mentor = models.ForeignKey(Mentore,on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='media', null=True)
    descripcionBrebe = models.TextField(null=True)
    descripcionAmplia = models.TextField(null=True)
    video = EmbedVideoField(null=True)
    dirigido_a_1 = models.TextField(null=True)
    modulo = models.TextField(null=True)

    
    
    def delete(self, *args,**kwargs):
         if os.path.isfile(self.imagen.path):
             os.remove(self.imagen.path)
         super(Curso, self).delete(*args, **kwargs)
            
    def __str__(self):
       return self.titulo
   