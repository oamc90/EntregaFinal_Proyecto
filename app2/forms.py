from django import forms
from datetime import datetime
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

class mensajeFormulario(forms.Form):
    usuarios=User.objects.all()
    lista_usuario=[]
    for usuarios in usuarios: 
        lista=(usuarios,usuarios)
        lista_usuario.append(lista)

    emisor= forms.CharField(max_length=50)
    receptor= forms.ChoiceField(choices=lista_usuario)
    contenido=forms.CharField(max_length=50)
    
 
 