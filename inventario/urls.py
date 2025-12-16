# -*- coding: utf-8 -*-
# vim:ts=4:expandtab:ai
# $Id: urls.py 20 2025-11-27 21:10:24Z vic@gssi.es $

from django.urls import path

app_name = 'inventario'

from .views import TipoList
from .views import TipoDetail
from .views import TipoCreate
from .views import TipoUpdate
from .views import TipoDelete
from .views import UbicacionList
from .views import UbicacionDetail
from .views import UbicacionCreate
from .views import UbicacionUpdate
from .views import UbicacionDelete
from .views import ObjetoList
from .views import ObjetoDetail
from .views import ObjetoCreate
from .views import ObjetoUpdate
from .views import ObjetoDelete

urlpatterns = [
    path('tipo', TipoList.as_view(), name='tipo-list'),
    path('tipo/add', TipoCreate.as_view(), name='tipo-create'),
    path('tipo/<int:pk>', TipoDetail.as_view(), name='tipo-detail'),
    path('tipo/<int:pk>/edit', TipoUpdate.as_view(), name='tipo-update'),
    path('tipo/<int:pk>/del', TipoDelete.as_view(), name='tipo-delete'),
    path('ubicacion', UbicacionList.as_view(), name='ubicacion-list'),
    path('ubicacion/add', UbicacionCreate.as_view(), name='ubicacion-create'),
    path('ubicacion/<int:pk>', UbicacionDetail.as_view(), name='ubicacion-detail'),
    path('ubicacion/<int:pk>/edit', UbicacionUpdate.as_view(), name='ubicacion-update'),
    path('ubicacion/<int:pk>/del', UbicacionDelete.as_view(), name='ubicacion-delete'),
    path('objeto', ObjetoList.as_view(), name='objeto-list'),
    path('objeto/add', ObjetoCreate.as_view(), name='objeto-create'),
    path('objeto/<int:pk>', ObjetoDetail.as_view(), name='objeto-detail'),
    path('objeto/<int:pk>/edit', ObjetoUpdate.as_view(), name='objeto-update'),
    path('objeto/<int:pk>/del', ObjetoDelete.as_view(), name='objeto-delete'),
    path('', ObjetoCreate.as_view(), name='objeto-create'),
]
