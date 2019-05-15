#!/usr/bin/python3
# encoding: utf-8
# @Time : 2019/3/2921:50
# @Author Superficial
# @File urls.py
# @Software PyCharm

from django.urls import re_path
from comments import views

app_name = 'comment'

urlpatterns = [
    re_path('^add/$', views.add_comment),
]
