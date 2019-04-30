#!/usr/bin/python3
# encoding: utf-8
# @Time : 2019/4/24 17:07
# @Author Superficial
# @File email.py
# @Software PyCharm

from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.template import loader
from django.conf import settings


class SendEmail:
    """发送邮件"""

    def send_html_email(self, subject, html_content, to_list):
        """
        发送HTML邮件
        :param subject: 邮件标题
        :param html_content: 邮件内容
        :param to_list: 收件人  list
        """
        send_from = settings.EMAIL_HOST_USER
        # 要发送的邮件来着那个用户
        message = EmailMessage(subject, html_content, send_from, to_list)
        message.content_subtype = 'html'
        # 设置类型为html
        message.send()

    def send_text_email(self, subject, content, to_list, is_fail_silently=False):
        """
        发送文本邮件
        :param subject: 邮件标题
        :param content: 邮件内容
        :param to_list: 收件人  list
        :param is_fail_silently: 是否抛出异常
        """
        send_from = settings.EMAIL_HOST_USER
        # 要发送的邮件来着那个用户
        send_mail(subject, content, send_from, to_list, fail_silently=is_fail_silently)

    def send_email_by_template(self, subject, module, data, to_list):
        """
        邮件模板
        :param subject: 邮件标题
        :param module: 模板名称
        :param data: 数据
        :param to_list: 收件人  list
        """
        html_content = loader.render_to_string(module, data)
        self.send_html_email(subject, html_content, to_list)
