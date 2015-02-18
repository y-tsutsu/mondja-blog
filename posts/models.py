"""
Definition of models.
"""

# coding: utf-8

from django.db import models

class Post(models.Model):
    title = models.CharField(max_length = 200)
    content = models.TextField(max_length = 10000)
    pub_date = models.DateTimeField('date published', auto_now_add = True)

    def __str__(self):
        return self.title

    def get_total(self):
        return len(self.content)

    def get_absolute_url(self):
        return '/entries/detail/{0}'.format(self.id)

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days = 1)

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'
