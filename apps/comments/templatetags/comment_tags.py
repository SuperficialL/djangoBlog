#!/usr/bin/python3
# encoding: utf-8
# @Time : 2019/4/25 17:53
# @Author Superficial
# @File comment_tags.py
# @Software PyCharm

from django import template
from django.db.models import Q
import hashlib
import urllib
from urllib.request import urlretrieve
from ..models import Comment

register = template.Library()


@register.simple_tag
def get_comment_count(article_id):
    """获取一个文章的评论总数"""
    return Comment.objects.filter(belong_id=article_id).count()


@register.simple_tag
def get_parent_comments(article_id, parent=None):
    """获取一个文章的父评论列表"""
    return Comment.objects.filter(belong_id=article_id, parent=parent)


@register.simple_tag
def get_child_comments(comment):
    """获取一个父评论的子评论列表"""
    child_comments = []

    def parse(parent):
        print(parent, type(parent), 'parent')
        childs = Comment.objects.filter(parent=parent)
        print(childs, 'child')
        for child in childs:
            child_comments.append(child)
            parse(child)

    parse(comment)
    return child_comments


@register.simple_tag
def get_comment_user_count(entry=0):
    """获取评论人总数"""
    p = []
    lis = Comment.objects.filter(belong_id=entry)
    for each in lis:
        if each.author not in p:
            p.append(each.author)
    return len(p)


# return only the URL of the gravatar
# TEMPLATE USE:  {{ email|gravatar_url:150 }}
@register.filter
def gravatar_url(email, size=40):
    """获得gravatar头像"""
    DEFAULT = '/media/avatar/default.jpg'
    user = Comment.objects.filter(email=email)
    if user:
        obj = list(filter(lambda x: x.avatar is not None, user))
        if obj:
            return obj[0].avatar
    email = email.encode('utf-8')
    url = "https://www.gravatar.com/avatar/%s?%s" % (
        hashlib.md5(email.lower()).hexdigest(), urllib.parse.urlencode({'d': DEFAULT, 's': str(size)}))
    return url
