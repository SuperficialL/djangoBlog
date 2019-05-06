#!/usr/bin/python3
# encoding: utf-8
# @Time : 2019/5/6 23:40
# @Author Superficial
# @File tasks.py
# @Software PyCharm
import django
from django.conf import settings
from django.core.mail import EmailMessage, send_mail
from celery import Celery
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoBlog.settings')
django.setup()

# 创建Celery类实例对象
app = Celery('celery_tasks.tasks', broker='redis://127.0.0.1:6379/8')


# 在我初步使用`celery`时,出现了问题,
# 我所使用的的开发环境
# 系统是
# 编辑工具,
# 1. `windows 7`64位
# 2. `PyCharm 2018.3.2 (Professional Edition)`
# 3. `Celery 4.3.0`

@app.task
def send_email_by_celery(subject, html_content, to_list, fail_silently=False):
    """
    异步发送邮件
    发送HTML邮件
    :param subject: 邮件标题
    :param html_content: 邮件内容
    :param send_from: 发件人
    :param to_list: 收件人  list
    :param fail_silently:
    :return:
    """
    send_from = settings.EMAIL_HOST_USER
    msg = EmailMessage(subject, html_content, send_from, to_list)
    msg.content_subtype = 'html'
    msg.send(fail_silently)


@app.task
def send_email_by(subject, html_content, recipient_list, fail_silently=True):
    """
    异步发送邮件
    :param subject: 字符串，表示邮件标题
    :param html_content: 邮件内容
    :param from_email: 字符串，表示发件邮箱。
    :param recipient_list: 字符串列表，列表中每个成员都是一个邮箱地址
    :param fail_silently: （可选）布尔值。为 False 时， send_mail 会抛出 smtplib.SMTPException 异常
    :return:
    """
    message = ''
    receiver = [recipient_list]
    from_email = settings.EMAIL_HOST_USER
    send_mail(subject, message, from_email, receiver, html_message=html_content)


@app.task
def hello():
    print('hello world~')
