# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import CaoDian


@admin.register(CaoDian)
class CaoDianAdmin(admin.ModelAdmin):
    pass
