#!/usr/bin/python3
# encoding: utf-8
# @Time : 2019/3/2921:15
# @Author Superficial
# @File forms.py
# @Software PyCharm


from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    article = forms.IntegerField(error_messages={"required": "必须传入评论文章的id！"})

    class Meta:
        model = Comment
        fields = ['name', 'email', 'url', 'content']
        exclude = ['article', 'avatar', 'parent', 'created_time', 'ip_addr', 'browser']
