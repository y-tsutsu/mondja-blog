"""
Definition of models.
"""

# coding: utf-8

import datetime
from django.db import models
from django.utils import timezone
from django.contrib.auth import models as usermodels

class PhotoImage(models.Model):
    description = models.CharField(max_length = 64)
    pub_date = models.DateTimeField('date published', auto_now_add = True)
    image = models.ImageField(upload_to = 'photo_images')
    user = models.ForeignKey(usermodels.User)

    def __str__(self):
        return self.description

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days = 1)

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'
