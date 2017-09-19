# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import
from django.shortcuts import render
from zutils.views import View
from caodian.models import CaoDian


class CaoDianView(View):
    model = CaoDian

    def list(self, request, *args, **kwargs):
        return render(request, template_name='caodian/list.html')
