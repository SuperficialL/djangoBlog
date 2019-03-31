#!/usr/bin/python3
# encoding: utf-8
# @Time : 2019/3/2921:50
# @Author Superficial
# @File urls.py
# @Software PyCharm
from django.urls import path
from apps.comments import views

app_name = 'comments'

urlpatterns = [
    path('add_comment/', views.add_comment, name='add_comment'),
]
