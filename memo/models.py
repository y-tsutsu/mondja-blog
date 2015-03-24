"""
Definition of models.
"""

# coding: utf-8

import datetime
from django.db import models
from django.utils import timezone
from django.contrib.auth import models as usermodels

class Tag(models.Model):
    name = models.TextField(max_length = 32, unique = True)
    pub_date = models.DateTimeField('date published', auto_now_add = True)
    user = models.ForeignKey(usermodels.User)

    def __str__(self):
        return self.name

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days = 1)

    def get_label_classname(self):
        n = hash(self)
        if n % 6 == 0:
            return 'label label-default'
        elif n % 6 == 1:
            return 'label label-primary'
        elif n % 6 == 2:
            return 'label label-success'
        elif n % 6 == 3:
            return 'label label-info'
        elif n % 6 == 4:
            return 'label label-warning'
        else:
            return 'label label-danger'

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

class Memo(models.Model):
    title = models.CharField(max_length = 200)
    content = models.TextField(max_length = 10000)
    pub_date = models.DateTimeField('date published', auto_now_add = True)
    user = models.ForeignKey(usermodels.User)
    tags = models.ManyToManyField(Tag, blank = True)

    def __str__(self):
        return self.title

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days = 1)

    def get_tags_str(self):
        return ' '.join([t.name for t in self.tags.all()])

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'
