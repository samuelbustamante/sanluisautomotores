# -*- coding: utf-8 -*-

from django.db import models

class Message(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
