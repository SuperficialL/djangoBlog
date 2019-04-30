#!/usr/bin/python3
# encoding: utf-8
# @Time : 2019/4/2415:48
# @Author Superficial
# @File feeds.py
# @Software PyCharm

from django.contrib.syndication.views import Feed
from django.conf import settings
from blog.models import Article


class Feeds(Feed):
    title = "RSS 订阅"
    description = settings.SITE_DESCRIPTION
    feed_url = 'https://www.lylinux.net/feed'
    link = "/"

    def items(self):
        return Article.objects.all()[:100]

    def item_title(self, item):
        return "【{}】{}".format(item.category, item.title)

    def item_description(self, item):
        return item.body_to_markdown()
