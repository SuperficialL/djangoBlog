#!/usr/bin/python3
# encoding: utf-8
# @Time : 2019/3/2921:15
# @Author Superficial
# @File forms.py
# @Software PyCharm


from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'url', 'text', 'avatar', 'content', 'article', 'ip_addr', 'browser', 'parent']
