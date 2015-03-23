# coding: utf-8

from django import template
from django.template.defaultfilters import stringfilter
from markdown import Markdown

md = Markdown() 

register = template.Library()
 
@register.filter
@stringfilter
def mark2html(value):
    return md.convert(value)
