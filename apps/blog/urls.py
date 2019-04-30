#!/usr/bin/python3
# encoding: utf-8
# @Time : 2019/3/3019:37
# @Author Superficial
# @File urls.py
# @Software PyCharm


from django.urls import path, re_path
from apps.blog import views
from apps.blog.views import IndexView, DetailView, CategoryView, TagView, ArchiveView

app_name = 'blog'

urlpatterns = [
    re_path('^$', IndexView.as_view(), name='index'),
    re_path(r'^category/(?P<nav_slug>.*?)/(?P<slug>.*?)$', CategoryView.as_view(),
            name='category'),
    re_path(r'tag/(?P<tag_name>.*?)/$', TagView.as_view(), name='tag'),
    path(r'detail/<int:article_id>.html', DetailView.as_view(), name='detail'),
    re_path(r'archive/$', ArchiveView.as_view(), name='archive'),  # 归档页面
    # 全文搜索
    # re_path(r'^search/$', MySearchView.as_view(), name='search'),
    re_path(r'^search/$', views.search, name='search'),
    re_path(r'^about/$', views.about, name='about'),
]
