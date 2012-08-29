# -*- coding: utf-8 -*-

from choices import *
from stdimage import StdImageField
from django.db import models
from django.contrib.auth.models import User

class CarManager(models.Manager):
    def get_query_set(self):
        return super(CarManager, self).get_query_set().filter(type_vehicle='1')

class MotorcycleManager(models.Manager):
    def get_query_set(self):
        return super(MotorcycleManager, self).get_query_set().filter(type_vehicle='2')

class Vehicle(models.Model):
    user = models.ForeignKey(User)
    type_vehicle = models.CharField(max_length=4, choices=VEHICLES)
    mark = models.CharField(max_length=30)
    model = models.CharField(max_length=30)
    year = models.PositiveIntegerField()
    description = models.TextField()
    location = models.CharField(max_length=4, choices=LOCATIONS)
    price = models.PositiveIntegerField()
    contact = models.CharField(max_length=30)
    image1 = StdImageField(u'Imagen: ', upload_to='./', size=(600, 800), thumbnail_size=(100, 75))
    image2 = StdImageField(upload_to='./', size=(600, 800), thumbnail_size=(100, 75), blank=True)
    image3 = StdImageField(upload_to='./', size=(600, 800), thumbnail_size=(100, 75), blank=True)
    image4 = StdImageField(upload_to='./', size=(600, 800), thumbnail_size=(100, 75), blank=True)

    objects = models.Manager()

    def __unicode__(self):
        return u'%s %s %d' % (self.mark, self.model, self.year)

    class Meta:
        ordering = ('-id',)
        verbose_name = u'Automotor'
        verbose_name_plural = u'Automotores'
