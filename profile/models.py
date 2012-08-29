# -*- coding: utf-8 -*-

from time import time
from random import random
from hashlib import md5
from datetime import date
from django.db import models
from django.core.mail import EmailMultiAlternatives
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.ForeignKey(User, unique=True)
    type_user = models.PositiveIntegerField()
    activation_key = models.CharField(max_length=32)

    def create_user(self, username, email, password):
        user = User.objects.create_user(username, email, password)
        user.is_active = False
        user.save()
        return user

    def set_activation_key(self):
        m = md5()
        m.update(str(time()) + str(random()))
        self.activation_key = m.hexdigest()

    def create_common_user(self, username, email, password):
        self.user = self.create_user(username, email, password)
        self.type_user = 1
        self.set_activation_key()
        self.save()

    def create_company_user(self, username, email, password):
        self.user = self.create_user(username, email, password)
        self.type_user = 2
        self.set_activation_key()
        self.save()

    def is_common_user(self):
        return self.type_user == 1

    def is_company_user(self):
        return self.type_user == 2

    def send_email(self, to, subject, txt_content, html_content=None):
        email = [self.user.email]
        msg = EmailMultiAlternatives(subject, txt_content, to, email)
        msg.attach_alternative(html_content, "text/html")
        msg.send()

    def activate(self):
        self.user.is_active = True
        self.activation_key = ''
        self.user.save()
        self.save()

