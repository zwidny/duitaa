# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings


class CaoDian(models.Model):
    """槽点-为吐槽尔生

    """
    content = models.TextField()
    user = models.ManyToManyField(to=settings.AUTH_USER_MODEL, related_name='caodian')

    @property
    def truncate(self):
        return 30

    def __str__(self):
        return "{}".format(self.content[:self.truncate])

    def __unicode__(self):
        return "{}".format(self.content[:self.truncate])
