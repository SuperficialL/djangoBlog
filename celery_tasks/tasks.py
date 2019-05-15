#!/usr/bin/python3
# encoding: utf-8
# @Time : 2019/5/6 23:40
# @Author Superficial
# @File tasks.py
# @Software PyCharm

from django.core.mail import EmailMessage
from django.template import loader
from celery_tasks import app


@app.task
def send_email_by_celery(subject, module, email_data, send_from, to_list, fail_silently=False):
    """
    接收的数据通过loader渲染成html字符串来发送模板邮件
    :param subject: 邮件标题
    :param module: 邮件模板(评论和回复)
    :param email_data: 渲染模型需要的数据
    :param send_from: 发送邮件的人
    :param to_list: 接收邮件的人,list
    :param fail_silently: 为 False时抛出异常,send_mail 会抛出 smtplib.SMTPException 异常
    """
    html_content = loader.render_to_string(module, email_data)
    msg = EmailMessage(subject, html_content, send_from, to_list)
    msg.content_subtype = "html"
    msg.send(fail_silently)
