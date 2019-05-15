from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class UserIP(models.Model):
    """访问网站的用户IP,访问页面,以及次数"""
    ip = models.CharField(verbose_name='IP地址',
                          max_length=30)
    ip_addr = models.CharField(verbose_name='IP地理位置',
                               max_length=30,
                               default='')
    end_point = models.CharField(verbose_name='访问端点',
                                 default='/',
                                 max_length=100)
    count = models.IntegerField(verbose_name='访问次数',
                                default=0)
    created_time = models.DateTimeField(verbose_name='最后访问时间',
                                        auto_now=True)

    class Meta:
        verbose_name = '访问用户信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.ip)


class DayNumber(models.Model):
    """网站单日访问量统计"""
    day = models.DateTimeField(verbose_name='日期',
                               auto_now_add=True)
    count = models.IntegerField(verbose_name='网站访问次数', default=0)

    class Meta:
        verbose_name = '网站日访问量统计'
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.day)


class OAuth(AbstractUser):
    """自定义用户模型"""
    DEFAULT = '/media/avatar/default.jpg'
    link = models.URLField('个人网址',
                           blank=True,
                           help_text='提示：网址必须填写以http开头的完整形式')
    avatar = models.ImageField(upload_to='avatar/%Y/%m/%d',
                               verbose_name='头像',
                               default=DEFAULT)

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name
        ordering = ['-id']

    def __str__(self):
        return str(self.username)
