from django.contrib import admin
from .models import Comment


# Register your models here.

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('nickname', 'email', 'url', 'belong', 'created_time', 'parent', 'browser', 'ip_address')
