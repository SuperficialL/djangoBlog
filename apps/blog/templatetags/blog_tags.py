#!/usr/bin/python3
# encoding: utf-8
# @Time : 2019/4/35:53
# @Author Superficial
# @File side_tags.py
# @Software PyCharm

from django import template
from ..models import Article, Category, Tag, Banner, FriendLink, Navigation, Notice, SiteInfo

register = template.Library()


@register.simple_tag
def get_navigation_list():
    """获取导航列表"""
    return Navigation.objects.all()


# 返回文章分类查询集
@register.simple_tag
def get_category_list(pk):
    """返回分类列表"""
    return Category.objects.filter(navigation=pk)


@register.simple_tag
def get_carousel_list():
    """获取轮播列表"""
    return Banner.objects.all()


@register.simple_tag
def get_hot_article():
    """获取热门文章"""
    return Article.objects.filter(status='p').order_by('views')[:10]


@register.simple_tag
def get_recent_article():
    """获取最近文章"""
    return Article.objects.filter(status='p').order_by('created_time')[:10]


@register.simple_tag
def get_recommend_article(article):
    """
    获取相关文章，排除自己
    :param article:
    :return:
    """
    tags = article.tags.all()
    article_list = []
    for tag in tags:
        for post in tag.article_set.filter(status='p'):
            if post != article:
                article_list.append(post)
    return article_list
