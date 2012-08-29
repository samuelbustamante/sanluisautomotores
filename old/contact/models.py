# -*- coding: utf-8 -*-

from django.db import models
from django.core.mail import EmailMultiAlternatives

class Message(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    message = models.TextField()
    offer = models.BooleanField()
    # Agregar las posición
    date = models.DateTimeField(auto_now=True)
    send_email = models.BooleanField(editable=False)

    def send_email(self, to, subject, txt_content, html_content=None):
        email = [self.email]
        msg = EmailMultiAlternatives(subject, txt_content, to, email)
        if html_content:
            msg.attach_alternative(html_content, "text/html")
        msg.send()
