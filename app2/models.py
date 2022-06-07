from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
# Create your models here.


class Mensaje(models.Model):
    emisor=models.CharField(max_length=50)
    receptor=models.CharField(max_length=50)
    contenido=RichTextField(blank=True, null=True)
    fecha_envio=models.TextField(default='dd/mm/aa')
    



