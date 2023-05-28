from typing import Any, Dict, Tuple
from django.db import models
import os

# Create your models here.
class Curso(models.Model):
    
    imagen = models.ImageField(upload_to='media', null=True)
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(null=True)
    descripcionDentro = models.TextField(null=True)
    video = models.TextField(null=True)
    consultor = models.CharField(max_length=100, null=True)
    imgconsultor = models.ImageField(upload_to='media', null=True)
    aprenderas = models.TextField(null=True)
    aprenderas2 = models.TextField(null=True)
    aprenderas3 = models.TextField(null=True)
    aprenderas4 = models.TextField(blank=True)
    
    


    def __str__(self):
     return self.nombre
 
    def delete(self, *args,**kwargs):
        if os.path.isfile(self.imagen.path):
            os.remove(self.imagen.path)
        super(Curso, self).delete(*args, **kwargs)
        
    def delete(self, *args,**kwargs):
        if os.path.isfile(self.imgconsultor.path):
            os.remove(self.imgconsultor.path)
        super(Curso, self).delete(*args, **kwargs)
            
       
    
        
        

class Tema(models.Model): 
    
    unidad = models.CharField(max_length=200)
    descripcion = models.TextField()
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    def __str__(self):
     return self.unidad