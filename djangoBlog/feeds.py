#!/usr/bin/python3
# encoding: utf-8
# @Time : 2019/4/2415:48
# @Author Superficial
# @File feeds.py
# @Software PyCharm

from django.contrib.syndication.views import Feed
from blog.models import Article
from blog.models import SiteInfo


class Feeds(Feed):
    title = "RSS 订阅"
    # description = SiteInfo.objects.all().first().description
    feed_url = 'https://www.zhangwuruil.com/feed'
    link = "/"

    def items(self):
        return Article.objects.all()

    def item_title(self, item):
        return "【{}】{}".format(item.category, item.title)

    def item_description(self, item):
        return item.body_to_markdown()
