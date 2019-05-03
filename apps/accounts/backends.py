#!/usr/bin/python3
# encoding: utf-8
# @Time : 2019/5/3 15:24
# @Author Superficial
# @File backends.py
# @Software PyCharm

from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission

User = get_user_model()


class CustomBackend(ModelBackend):
    """自定义后台验证"""

    def authenticate(self, request, username=None, password=None, **kwargs):
        """
        重写authenticate方法
        :param request: http请求
        :param username: 用户名
        :param password: 密码
        :param kwargs: 其余参数
        :return: 返回用户
        """
        user = User.objects.filter(Q(username=username) | Q(email=username)).first()
        if user:
            if user.check_password(password):
                return user
        return None
