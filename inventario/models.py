from django.db import models

# Create your models here.
import datetime
import logging
import pytz
import traceback
import uuid

#from django.conf import settigs
#from django.contrib.auth.models import Users
from django.template.defaultfilters import floatformat
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils import translation
from django.utils.encoding import smart_str
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from django.utils.translation import gettext as __

class Ubicacion(models.Model):
    nombre = models.CharField(
        max_length=50, db_index=True, verbose_name=_('Nombre')
    )
    descripcion = models.TextField(
        blank = True, null=True, verbose_name=_('Descripción')
    )


class Tipo(models.Model):
    nombre = models.CharField(
        max_length=50, db_index=True, verbose_name=_('Nombre')
    )

    descripcion = models.CharField(
        max_length=250, blank=True, null=True, verbose_name=_('Descripcion')
    ) 



class Objeto(models.Model):
    tipo = models.ForeignKey(
        Tipo, on_delete=models.PROTECT, verbose_name=_('Tipo')
    )

    etiqueta = models.UUIDField( 
        db_index=True, verbose_name=_('Etiqueta'),
        default=uuid.uuid4,
        editable=False 
    )
    
    nombre = models.CharField(
        max_length = 200, db_index=True, verbose_name=_('Nombre')
    )
    
    valor = models.FloatField(
        verbose_name=_('Valor'), default=0.0    
    )

    descripcion=models.TextField(
        blank=True, null=True, verbose_name=_('Descripción')
    )

    def __str__(self):
        return f'{self.nombre}'
    
