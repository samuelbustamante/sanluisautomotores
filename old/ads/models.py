# -*- coding: utf-8 -*-

import datetime
from django.db import models
from myproject.choices.models import Currency

class TypeAd(models.Model):
    name = models.CharField(max_length=30)
    price = models.PositiveIntegerField()
    currency = models.ForeignKey(Currency)
    number_images = models.PositiveIntegerField()
    number_days = models.PositiveIntegerField()
    priority = models.PositiveIntegerField()

    class Meta:
        ordering = ('priority',)
        verbose_name = u'Tipo de Anuncio'
        verbose_name_plural = u'Tipos de Anuncios'

class Ad(models.Model):
    type = models.ForeignKey(TypeAd)
    published = models.DateTimeField(auto_now=True)
    finished = models.DateTimeField(default=datetime.datetime.now())

    def update_finished(self):
        self.finished = self.published + datetime.timedelta(days=self.type.number_days)
        self.save()

    class Meta:
        ordering = ('type', '-published')
        verbose_name = u'Anuncio'
        verbose_name_plural = u'Anucios'
