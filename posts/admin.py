# coding: utf-8

from django.contrib import admin
from posts.models import Post, Comment

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1

class PostAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Title',              {'fields':['title']}),
        ('Detail information', {'fields':['content'], 'classes':['collapse']}),
    ]
    list_display = ('title', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['title']
    date_hierarchy = 'pub_date'
    inlines = [CommentInline]

admin.site.register(Post, PostAdmin)
