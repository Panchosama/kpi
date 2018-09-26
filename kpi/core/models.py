# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from smart_selects.db_fields import ChainedForeignKey

# Create your models here.
@python_2_unicode_compatible
class Area(models.Model):
	nombre=models.CharField(max_length=100, unique=True)
	descripcion=models.TextField()

	def __str__(self):
		return self.nombre

@python_2_unicode_compatible
class Departamento(models.Model):
	nombre=models.CharField(max_length=100, unique=True)
	area=models.ForeignKey('Area', null=True)
	descripcion=models.TextField()

	def __str__(self):
		return self.nombre

@python_2_unicode_compatible
class Norma(models.Model):
	entidad=models.CharField(max_length=10, null=True)
	nombre=models.TextField()
	codigo=models.PositiveSmallIntegerField(default=0)
	version=models.PositiveSmallIntegerField(default=0)

	def __str__(self):
		return self.entidad+" "+str(self.codigo)+":"+str(self.version)

@python_2_unicode_compatible
class Tipo(models.Model):
	nombre=models.CharField(max_length=50, unique=True)
	descripcion=models.TextField(null=True)

	def __str__(self):
		return self.nombre


@python_2_unicode_compatible
class Cargo(models.Model):
	nombre=models.CharField(max_length=100, unique=True)
	departamento=models.ForeignKey('Departamento', null=True)
	descripcion=models.TextField(null=True)

	def __str__(self):
		return self.nombre

@python_2_unicode_compatible
class Proceso(models.Model):
	nombre=models.CharField(max_length=100, unique=True)
	area=models.ForeignKey('Area',null=True)
	departamento=ChainedForeignKey(
		Departamento, 
		chained_field='area',
		chained_model_field='area',
		show_all=False,
		null=True)
	responsable=ChainedForeignKey(
		Cargo, 
		chained_field='departamento',
		chained_model_field='departamento',
		show_all=False,
		null=True)
	objetivo=models.TextField(null=True)

	def __str__(self):
		return self.nombre
	
@python_2_unicode_compatible
class Indicador(models.Model):
	nombre=models.CharField(max_length=100, unique=True)
	proceso=models.ForeignKey('Proceso')
	tipo=models.ForeignKey('Tipo')
	norma=models.ForeignKey('Norma')
	descripcion=models.TextField()
	medicion=models.CharField(max_length=50)
	rango_esp=models.DecimalField(max_digits=5,decimal_places=2)
	rango_mid=models.DecimalField(max_digits=5,decimal_places=2)
	rango_max=models.DecimalField(max_digits=5,decimal_places=2)
	creado=models.DateField(auto_now_add=True)
	modificado=models.DateField(auto_now=True)

	def __str__(self):
		return self.nombre
