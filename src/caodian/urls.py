# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import
from django.conf.urls import url
from caodian.views import caodian

urlpatterns = [
    url(r'^$', caodian.CaoDianView.as_view(func='list'), name='list'),
]
