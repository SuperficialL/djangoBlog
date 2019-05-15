#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/11 12:53
# @Author  : Superficial
# @File    : signals.py
# @Software: PyCharm

from django.db.models.signals import post_save
from django.dispatch import receiver
import requests
from blog.models import Article
import logging

logger = logging.getLogger(__name__)


@receiver(post_save, sender=Article)
def article_save(sender, instance, created=False, **kwargs):
    """保存文章时通知百度"""
    if not created:
        try:
            url = 'http://data.zz.baidu.com/urls?site=www.zhangwurui.com&token=ZwW1JLUTRYQeZ2XE'
            data = '\n'.join(instance.get_absolute_url())
            res = requests.post(url, data=data)
            logger.info(res.text)
        except Exception as e:
            logger.error(e)
