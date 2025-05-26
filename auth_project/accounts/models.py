from django.db import models
from django.contrib.auth.models import User

class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        permissions = [
            ("can_publish", "Can Publish Posts"),
        ]

    def __str__(self):
        return self.title
    
"""
La clase interna Meta en un modelo de Django 
te permite configurar una gran variedad de 
opciones que afectan cómo se comporta ese 
modelo en la base de datos, en las consultas, 
en el admin, etc.



"""
