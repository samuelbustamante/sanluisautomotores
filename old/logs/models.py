# -*- coding: utf-8 -*-

from django.db import models

class Log(models.Model):
    created = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)

    def __unicode__(self):
        return u'%s - %s - %s' % (self.created, self.title, self.description)

    def write(self, title, description):
        self.title = title
        self.description = description
        self.save()
