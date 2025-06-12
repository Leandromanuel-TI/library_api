from django.contrib import admin
from django.contrib import admin
from .models import Cliente, Equipamento, Tecnico, Reparacao

admin.site.register(Cliente)
admin.site.register(Equipamento)
admin.site.register(Tecnico)
admin.site.register(Reparacao)


# Register your models here.
