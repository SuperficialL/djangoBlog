from django.db import models
from apps.blog.models import Article
from django.conf import settings
from urllib.request import urlretrieve
import hashlib


# Create your models here.

class Comment(models.Model):
    """评论"""
    name = models.CharField(verbose_name='评论者',
                            max_length=30)
    email = models.EmailField(verbose_name='邮箱',
                              blank=False)
    avatar = models.ImageField(verbose_name='用户头像',
                               blank=True,
                               max_length=255)
    url = models.URLField(verbose_name='网站地址',
                          blank=True)
    content = models.TextField(verbose_name='评论内容',
                               blank=True,
                               null=True)
    article = models.ForeignKey(Article,
                                on_delete=models.CASCADE,
                                verbose_name='所属文章')
    ip_addr = models.CharField(verbose_name='IP地址',
                               max_length=100,
                               default='')
    browser = models.CharField(verbose_name='浏览器',
                               max_length=100,
                               default='')
    created_time = models.DateTimeField(verbose_name='评论时间',
                                        auto_now=True)
    parent = models.ForeignKey('self',
                               verbose_name='父评论',
                               blank=True,
                               null=True,
                               on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        """获取用户头像并保存URL 用户头像路径"""
        user = Comment.objects.filter(email=self.email)
        print(user)
        if user:
            print('用户头像将使用已有的')
            avatar_url = Comment.objects.filter(email=self.email).values('avatar')
            self.avatar = avatar_url
        avatar_url = ''.join(['http://www.gravatar.com/avatar/',
                              hashlib.md5(self.email.lower().encode('utf-8')).hexdigest(), '?s=%d' % 64])
        # 头像文件名
        name = r'{}.jpg'.format(self.name)
        # 保存用户头像到后台头像文件中
        urlretrieve(avatar_url, filename=settings.MEDIA_ROOT + r'/avatar/' + name)
        self.avatar = r'/avatar/' + name
        super(Comment, self).save(*args, **kwargs)
        print("用户头像保存成功")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created_time']
        verbose_name = '评论'
        verbose_name_plural = verbose_name
