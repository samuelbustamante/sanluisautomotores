# -*- coding: utf-8 -*-

from django.db import models
from myproject.logs.models import Log

class Cash(models.Model):
    cash = models.PositiveIntegerField()

    def __unicode__(self):
        return u'%d' % self.cash

    def add_cash(self, cash):
        log = Log()
        try:
            balance = self.cash
            self.cash  = balance + cash
            self.save()
            log.write(u'succesfull [add cash]',
                      u'old_balance: %d | add: %d | new_balance: %d' %\
                     (balance, cash, self.cash))
        except:
            log.write(u'error [add cash]',
                      u'add: %d | balance: %d' % (cash, self.cash))

    def subtract_cash(self, cash):
        log = Log()
        try:
            balance = self.cash
            self.cash = balance - cash
            self.save()
            log.write(u'succesfull [add cash]',
                      u'old_balance: %d | add: %d | new_balance: %d' %\
                     (balance, cash, self.cash))
        except:
            log.write(u'error [add cash]',
                      u'add: %d | balance: %d' % (cash, self.cash))
