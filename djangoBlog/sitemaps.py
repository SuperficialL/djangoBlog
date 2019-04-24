#!/usr/bin/python3
# encoding: utf-8
# @Time : 2019/4/24 13:01
# @Author Superficial
# @File sitemaps.py
# @Software PyCharm

from django.contrib.sitemaps import Sitemap
from apps.blog.models import Article, Category, Tag
from django.urls import reverse


class ArticleSiteMap(Sitemap):
    """
        changefreq 更新频率
        priority 相对于其它页面的优先权
    """
    changefreq = "monthly"
    priority = "0.6"

    def items(self):
        return Article.objects.all()

    def lastmod(self, obj):
        """上次修改时间"""
        return obj.modified_time

    def location(self, obj):
        """可选.返回每个对象的绝对路径.如果对象有get_absolute_url()方法,可以省略location"""
        return reverse('blog:detail', kwargs={'pk': int(obj.id)})


class CategorySiteMap(Sitemap):
    """
        changefreq 更新频率
        priority 相对于其它页面的优先权
    """
    changefreq = "Weekly"
    priority = "0.6"

    def items(self):
        return Category.objects.all()

    def lastmod(self, obj):
        return obj.modified_time

    def location(self, obj):
        """可选.返回每个对象的绝对路径.如果对象有get_absolute_url()方法,可以省略location"""
        return reverse('blog:category', kwargs={'pk': int(obj.id)})


class TagSiteMap(Sitemap):
    """
        changefreq 更新频率
        priority 相对于其它页面的优先权
    """
    changefreq = "Weekly"
    priority = "0.3"

    def items(self):
        return Tag.objects.all()

    def lastmod(self, obj):
        return obj.modified_time

    def location(self, obj):
        """可选.返回每个对象的绝对路径.如果对象有get_absolute_url()方法,可以省略location"""
        return reverse('blog:tags', kwargs={'pk': obj.id})
