#!/usr/bin/python3
# encoding: utf-8
# @Time : 2019/5/6 23:40
# @Author Superficial
# @File __init__.py.py
# @Software PyCharm

import os
import django
from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoBlog.settings')
# 用来解决windows下ValueError
# ValueError: not enough values to unpack (expected 3, got 0)
os.environ.setdefault('FORKED_BY_MULTIPROCESSING', '1')

# 创建Celery类实例对象
app = Celery('celery_tasks')

# 通过实例加载配置
app.config_from_object('django.conf:settings')
# 指定celery配置文件

# 搜索django应用下的所有任务
app.autodiscover_tasks()
