# -*- coding: utf-8 -*-
# vim:ts=4:expandtab:ai
# $Id: admin.py 23 2025-11-28 01:22:56Z vic@gssi.es $

from django.contrib import admin


from .models import Tipo
from .models import Objeto
from .models import Ubicacion

class ObjetoInlineTipo(admin.TabularInline):
    model = Objeto
    fields = ['etiqueta', 'nombre', 'ubicacion', 'valor']
    list_filter = ['ubicacion']
    extra = 1


class ObjetoInlineDonde(admin.TabularInline):
    model = Objeto
    fields = ['tipo', 'etiqueta', 'nombre', 'valor']
    list_filter = ['tipo']
    extra = 1


@admin.register(Tipo)
class TipoAdmin(admin.ModelAdmin):
    list_display = ['pk', 'nombre']
    list_editable = ['nombre']
    readonly_fields = ['feccre', 'fecmod', 'creadopor', 'modificadopor']
    list_filter = ['feccre', 'fecmod', 'creadopor', 'modificadopor']
    save_on_top = True

    inlines = [ObjetoInlineTipo]

    fieldsets = (
        (
            None,
            {'fields': ['nombre', 'descripcion']},
        ),
        (
            'Registro',
            {
                'fields': ['feccre', 'fecmod', 'creadopor', 'modificadopor'],
                'classes': ('collapse',),
            },
        ),
    )

    def save_model(self, request, obj, form, change):
        if change:
            obj.modificadopor = request.user
        else:
            obj.creadopor = request.user
        super().save_model(request, obj, form, change)


@admin.register(Ubicacion)
class UbicacionAdmin(admin.ModelAdmin):
    list_display = ['pk', 'nombre']
    list_editable = ['nombre']
    readonly_fields = ['feccre', 'fecmod', 'creadopor', 'modificadopor']
    list_filter = ['feccre', 'fecmod', 'creadopor', 'modificadopor']
    save_on_top = True

    inlines = [ObjetoInlineDonde]

    fieldsets = (
        (
            None,
            {'fields': ['nombre', 'descripcion']},
        ),
        (
            'Registro',
            {
                'fields': ['feccre', 'fecmod', 'creadopor', 'modificadopor'],
                'classes': ('collapse',),
            },
        ),
    )

    def save_model(self, request, obj, form, change):
        if change:
            obj.modificadopor = request.user
        else:
            obj.creadopor = request.user
        super().save_model(request, obj, form, change)


@admin.register(Objeto)
class ObjetoAdmin(admin.ModelAdmin):
    list_display = ['pk', 'tipo', 'etiqueta', 'nombre', 'ubicacion', 'valor']
    list_editable = ['tipo', 'etiqueta', 'nombre', 'ubicacion', 'valor']
    readonly_fields = ['feccre', 'fecmod', 'creadopor', 'modificadopor']
    list_filter = ['tipo', 'ubicacion', 'feccre', 'fecmod', 'creadopor', 'modificadopor']
    search_fields = ['nombre', 'etiqueta']

    fieldsets = (
        (
            None,
            {
                'fields': [
                    ('tipo', 'etiqueta', 'nombre', 'ubicacion', 'valor'),
                    'descripcion',
                ]
            },
        ),
        (
            'Registro',
            {
                'fields': ['feccre', 'fecmod', 'creadopor', 'modificadopor'],
                'classes': ('collapse',),
            },
        ),
    )

    def save_model(self, request, obj, form, change):
        if change:
            obj.modificadopor = request.user
        else:
            obj.creadopor = request.user
        super().save_model(request, obj, form, change)




