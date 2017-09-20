# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import
from datetime import datetime
from haystack import indexes
from .models import CaoDian


class CaoDianIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    user = indexes.CharField(model_attr='user')
    created = indexes.DateTimeField(model_attr='created')

    def get_model(self):
        return CaoDian

    def index_queryset(self, using=None):
        return self.get_model().objects.filter(created__gte=datetime.now())
