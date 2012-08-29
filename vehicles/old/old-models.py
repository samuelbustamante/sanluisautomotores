# -*- coding: utf-8 -*-

from django.db import models
from myproject.ads.models import Ad
from myproject.profile.models import Profile
from myproject.gallery.models import Gallery
from myproject.profile.models import Profile
from myproject.choices.models import Location, Year, Currency, Color

#-------- Vehicle -------#

class Vehicle(models.Model):
    title = models.CharField(max_length=30)
    profile = models.ForeignKey(Profile)
    ad = models.ForeignKey(Ad)
    year = models.ForeignKey(Year)
    location = models.ForeignKey(Location)
    price = models.PositiveIntegerField()
    currency = models.ForeignKey(Currency)
    color = models.ForeignKey(Color)
    gallery = models.ForeignKey(Gallery)

    def get_price(self):
        return u'%s%d' % (self.currency.sign, self.price)

    class Meta:
        ordering = ('ad',)
        verbose_name = u'Automotor'
        verbose_name_plural = u'Automotores'

#---------- Car ----------#

class Car(Vehicle):
    type = models.ForeignKey('TypeCar')
    mark = models.ForeignKey('MarkCar')
    model = models.CharField(max_length=30)
    version = models.CharField(max_length=30)
    km = models.ForeignKey('KmCar')
    direction = models.ForeignKey('DirectionCar')
    transmission = models.ForeignKey('TransmissionCar')
    fuel = models.ForeignKey('FuelCar')
    doors = models.ForeignKey('DoorsCar')

    def __unicode__(self):
        return u'%s %s %s' % (self.mark, self.model, self.version)

    def get_characteristics(self):
        return u'%s, %s, %s puertas, %s' %\
                (self.year, self.km, self.doors, self.fuel)

    class Meta:
        ordering = ('-id',)
        verbose_name = u'Auto'
        verbose_name_plural = u'Autos'

class TypeCar(models.Model):
    name = models.CharField(max_length=30)

    def __unicode__(self):
        return u'%s' % self.name

    class Meta:
        ordering = ('name',)
        verbose_name = 'Tipo'
        verbose_name_plural = u'Autos - Tipos'

class MarkCar(models.Model):
    name = models.CharField(max_length=30)

    def __unicode__(self):
        return u'%s' % self.name

    class Meta:
        ordering = ('name',)
        verbose_name = 'Marca'
        verbose_name_plural = u'Autos - Marcas'

class KmCar(models.Model):
    name = models.CharField(max_length=30)

    def __unicode__(self):
        return u'%s' % self.name

    class Meta:
        ordering = ('name',)
        verbose_name = 'Kilometraje'
        verbose_name_plural = u'Autos - Kilometrajes'

class DirectionCar(models.Model):
    name = models.CharField(max_length=30)

    def __unicode__(self):
        return u'%s' % self.name

    class Meta:
        ordering = ('name',)
        verbose_name = 'Dirección'
        verbose_name_plural = u'Autos - Tipos de Dirección'

class TransmissionCar(models.Model):
    name = models.CharField(max_length=30)

    def __unicode__(self):
        return u'%s' % self.name

    class Meta:
        ordering = ('name',)
        verbose_name = 'Transmision'
        verbose_name_plural = u'Autos - Tipos de Transmisiones'

class FuelCar(models.Model):
    name = models.CharField(max_length=30)

    def __unicode__(self):
        return u'%s' % self.name

    class Meta:
        ordering = ('name',)
        verbose_name = 'Combustle'
        verbose_name_plural = u'Autos - Tipos de Combustibles'

class DoorsCar(models.Model):
    name = models.CharField(max_length=30)

    def __unicode__(self):
        return u'%s' % self.name

    class Meta:
        ordering = ('name',)
        verbose_name = 'Cantidad de puertas'
        verbose_name_plural = u'Autos - Cantidades de Puertas'

#------- Motorcycle -------#

class Motorcycle(Vehicle):
    type = models.ForeignKey('TypeMotorcycle')
    mark = models.ForeignKey('MarkMotorcycle')
    version = models.CharField(max_length=30)
    km = models.ForeignKey('KmMotorcycle')
    cylinder = models.ForeignKey('CilinderMotorcycle')
    brake = models.ForeignKey('BrakeMotorcycle')
    starting_system = models.ForeignKey('StartingSystemMotorcycle')
    type_motor = models.ForeignKey('TypeMotorMotorcycle')

    class Meta:
        ordering = ('-id',)
        verbose_name = u'Moto'
        verbose_name_plural = u'Motos'

class TypeMotorcycle(models.Model):
    name = models.CharField(max_length=30)

    def __unicode__(self):
        return u'%s' % self.name

    class Meta:
        ordering = ('name',)
        verbose_name = 'Tipo'
        verbose_name_plural = u'Motos - Tipos'

class MarkMotorcycle(models.Model):
    name = models.CharField(max_length=30)

    def __unicode__(self):
        return u'%s' % self.name

    class Meta:
        ordering = ('name',)
        verbose_name = 'Marca'
        verbose_name_plural = u'Motos - Marcas'

class KmMotorcycle(models.Model):
    name = models.CharField(max_length=30)

    def __unicode__(self):
        return u'%s' % self.name

    class Meta:
        ordering = ('name',)
        verbose_name = u'Kilometraje'
        verbose_name_plural = u'Motos - Kilometrajes'

class CilinderMotorcycle(models.Model):
    name = models.CharField(max_length=30)

    def __unicode__(self):
        return u'%s' % self.name

    class Meta:
        ordering = ('name',)
        verbose_name = u'Cilindrada'
        verbose_name_plural = u'Motos - Cilindradas'

class BrakeMotorcycle(models.Model):
    name = models.CharField(max_length=30)

    def __unicode__(self):
        return u'%s' % self.name

    class Meta:
        ordering = ('name',)
        verbose_name = u'Freno'
        verbose_name_plural = u'Motos - Frenos'

class StartingSystemMotorcycle(models.Model):
    name = models.CharField(max_length=30)

    def __unicode__(self):
        return u'%s' % self.name

    class Meta:
        ordering = ('name',)
        verbose_name = u'Sistema de Arranque'
        verbose_name_plural = u'Motos - Sistemas de Arranque'

class TypeMotorMotorcycle(models.Model):
    name = models.CharField(max_length=30)

    def __unicode__(self):
        return u'%s' % self.name

    class Meta:
        ordering = ('name',)
        verbose_name = u'Motor'
        verbose_name_plural = u'Motos - Motores'
