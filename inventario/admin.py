from django.contrib import admin

from .models import Tipo
from .models import Ubicacion
from .models import Objeto

admin.site.register(Objeto)
admin.site.register(Tipo)
admin.site.register(Ubicacion)
