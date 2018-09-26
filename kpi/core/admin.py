# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Departamento, Norma, Proceso, Indicador, Tipo, Area, Cargo

class DepartamentoAdmin(admin.ModelAdmin):
	list_display = ('nombre','area')
	list_filter = ['area']

class NormaAdmin(admin.ModelAdmin):
	list_display = ('__str__','nombre')
	
class CargoAdmin(admin.ModelAdmin):
	list_display=('nombre','departamento')
	list_filter=['departamento']

class ProcesoAdmin(admin.ModelAdmin):
	list_display=('nombre','area','departamento','responsable')
	list_filter=['area','departamento']

# Register your models here.
admin.site.register(Departamento, DepartamentoAdmin)
admin.site.register(Norma, NormaAdmin)
admin.site.register(Proceso, ProcesoAdmin)
admin.site.register(Indicador)
admin.site.register(Tipo)
admin.site.register(Area)
admin.site.register(Cargo, CargoAdmin)