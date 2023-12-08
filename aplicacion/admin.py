from django.contrib import admin

from aplicacion.models import Administrador, Bombero, Camioneta, Chofer

admin.site.register(Administrador)
admin.site.register(Bombero)
admin.site.register(Chofer)
admin.site.register(Camioneta)