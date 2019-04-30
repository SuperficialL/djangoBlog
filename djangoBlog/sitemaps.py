#!/usr/bin/python3
# encoding: utf-8
# @Time : 2019/4/24 13:01
# @Author Superficial
# @File sitemaps.py
# @Software PyCharm

from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from django.db.models.aggregates import Count
from blog.models import Article, Category, Tag


class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return ['blog:index']

    def location(self, item):
        return reverse(item)


class ArticleSiteMap(Sitemap):
    """
        changefreq 更新频率
        priority 相对于其它页面的优先权
    """
    changefreq = "monthly"
    priority = "1.0"

    def items(self):
        return Article.objects.filter(status='p')

    def lastmod(self, obj):
        """上次修改时间"""
        return obj.updated_time


class CategorySiteMap(Sitemap):
    """
        changefreq 更新频率
        priority 相对于其它页面的优先权
    """
    changefreq = "Weekly"
    priority = "0.6"

    def items(self):
        return Category.objects.annotate(total_num=Count('article')).filter(total_num__gt=0)

    def lastmod(self, obj):
        return obj.article_set.first().updated_time


class TagSiteMap(Sitemap):
    """
        changefreq 更新频率
        priority 相对于其它页面的优先权
    """
    changefreq = "Weekly"
    priority = "0.3"

    def items(self):
        return Tag.objects.annotate(total_num=Count('article')).filter(total_num__gt=0)

    def lastmod(self, obj):
        return obj.article_set.first().updated_time
