#!/usr/bin/python3
# encoding: utf-8
# @Time : 2019/3/2921:15
# @Author Superficial
# @File forms.py
# @Software PyCharm


from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    belong = forms.IntegerField(error_messages={"required": "必须传入评论文章的id！"})
    parent = forms.IntegerField(error_messages={"required": "必须传入用户的评论id！"})

    class Meta:
        model = Comment
        fields = ['nickname', 'email', 'url', 'content']
        exclude = ['belong', 'created_time', 'parent', 'ip_address', 'browser']
