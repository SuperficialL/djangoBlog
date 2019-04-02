from django.db import models
from django.utils import timezone


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
                                        default=timezone.now)

    def viewed(self):
        """更新用户访问量"""
        self.count += 1
        self.save(update_fields=['count'])

    class Meta:
        verbose_name = '访问用户信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.ip


class VisitNumber(models.Model):
    """网站访问总次数"""
    count = models.IntegerField(verbose_name='网站访问总次数', default=0)

    def update(self):
        """更新用户访问量"""
        self.save(update_fields=['count'])

    class Meta:
        verbose_name = '网站访问总次数'
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.count)


class DayNumber(models.Model):
    """网站单日访问量统计"""
    day = models.DateTimeField(verbose_name='日期',
                               default=timezone.now)
    count = models.IntegerField(verbose_name='网站访问次数', default=0)

    def update(self):
        """更新用户访问量"""
        self.save(update_fields=['count'])

    class Meta:
        verbose_name = '网站日访问量统计'
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.day)
