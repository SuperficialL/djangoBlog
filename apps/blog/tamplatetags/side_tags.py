#!/usr/bin/python3
# encoding: utf-8
# @Time : 2019/4/35:53
# @Author Superficial
# @File side_tags.py
# @Software PyCharm

from django import template
from apps.blog.models import Article, Tag, Category
from apps.comments.models import Comment
from apps.accounts.models import VisitNumber

register = template.Library()


@register.simple_tag()
def site_info():
    article_counts = Article.objects.all().count()
    comment_counts = Comment.objects.all().count()
    tag_counts = Tag.objects.all().count()
    category_counts = Category.objects.all().count()
    visit_count = VisitNumber.objects.all().count()
