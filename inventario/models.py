from django.db import models

# Create your models here.
import datetime
import logging
import pytz
import traceback
import uuid

#from django.conf import settigs
from django.contrib.auth.models import User
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

    feccre = models.DateTimeField(
        verbose_name=_('Creado'),
        auto_now_add=True,
        db_index=True,
        editable=False,
    )
    fecmod = models.DateTimeField(
        verbose_name=_('Modificado'),
        auto_now=True,
        db_index=True,
        editable=False,
    )
    creadopor = models.ForeignKey(
        User,
        verbose_name=_('Creado por'),
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        editable=False,
        related_name='ubicaciones_creadas',
    )
    modificadopor = models.ForeignKey(
        User,
        verbose_name=('Modificado por'),
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        editable=False,
        related_name='ubicaciones_modificadas',
        
    )
    class Meta:
        verbose_name=_('Ubicación')
        verbose_name_plural=_('Ubicaciones')
        ordering=['nombre']

    def __str__(self):
        return f'{self.nombre}'



class Tipo(models.Model):
    nombre = models.CharField(
        max_length=50, db_index=True, verbose_name=_('Nombre')
    )

    descripcion = models.TextField(
        blank=True, null=True, verbose_name=_('Descripcion')
    ) 
    feccre = models.DateTimeField(
        verbose_name=_('Creado'),
        auto_now_add=True,
        db_index=True,
        editable=False,
    )
    fecmod = models.DateTimeField(
        verbose_name=_('Modificado'),
        auto_now=True,
        db_index=True,
        editable=False,
    )
    creadopor = models.ForeignKey(
        User,
        verbose_name=_('Creado por'),
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        editable=False,
        related_name='tipos_creados',
    )
    modificadopor = models.ForeignKey(
        User,
        verbose_name=('Modificado por'),
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        editable=False,
        related_name='tipos_modificados',
        
    )
    class Meta:
        ordering = ['nombre']

    def __str__(self):
        return f'{self.nombre}'



class Objeto(models.Model):
    tipo = models.ForeignKey(
        Tipo, on_delete=models.PROTECT, verbose_name=_('Tipo')
    )
    ubicacion = models.ForeignKey(
        Ubicacion, 
        on_delete=models.PROTECT, 
        verbose_name=_('Ubicacion')
    )
    etiqueta = models.UUIDField( 
        db_index=True,
        verbose_name=_('Etiqueta'),
        default=uuid.uuid4,
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
    feccre = models.DateTimeField(
        verbose_name=_('Creado'),
        auto_now_add=True,
        db_index=True,
        editable=False,
    )
    fecmod = models.DateTimeField(
        verbose_name=_('Modificado'),
        auto_now=True,
        db_index=True,
        editable=False,
    )
    creadopor = models.ForeignKey(
        User,
        verbose_name=_('Creado por'),
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        editable=False,
        related_name='objetos_creados',
    )
    modificadopor = models.ForeignKey(
        User,
        verbose_name=('Modificado por'),
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        editable=False,
        related_name='objetos_modificados',
        
    )

    class Meta:
        ordering=['ubicacion','nombre']
    def __str__(self):
        return f'{self.nombre}'
    
