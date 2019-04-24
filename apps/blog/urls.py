#!/usr/bin/python3
# encoding: utf-8
# @Time : 2019/3/3019:37
# @Author Superficial
# @File urls.py
# @Software PyCharm


from django.urls import path
from apps.blog import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    path('category/<int:pk>', views.category, name='category'),
    path('detail/<int:pk>', views.detail, name='detail'),
    path('tag/<int:pk>', views.tag, name='tags'),
    path('search/', views.search, name='search'),
    path('about/', views.about, name='about'),
]
