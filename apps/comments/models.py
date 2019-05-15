from django.db import models
from blog.models import Article


# Create your models here.


class Comment(models.Model):
    """游客评论"""
    nickname = models.CharField(max_length=20, verbose_name='昵称')
    email = models.CharField(max_length=30, verbose_name='邮箱')
    avatar = models.URLField(verbose_name='头像', null=True, blank=True)
    url = models.CharField(max_length=200, verbose_name='地址', blank=True)
    created_time = models.DateTimeField('创建时间', auto_now_add=True)
    content = models.TextField('评论内容')
    browser = models.CharField('浏览器', max_length=200)
    ip_address = models.CharField('IP地址', max_length=200)
    parent = models.ForeignKey('self',
                               verbose_name='父评论',
                               on_delete=models.CASCADE,
                               related_name='%(class)s_child_comments',
                               blank=True,
                               null=True)
    belong = models.ForeignKey(Article,
                               on_delete=models.CASCADE,
                               related_name='article_comments',
                               verbose_name='所属文章')

    class Meta:
        verbose_name = '文章评论'
        verbose_name_plural = verbose_name
        ordering = ['-created_time']

    def get_child_comments(self):
        """获取子评论"""
        return Comment.objects.filter(belong_id=self.belong)

    def __str__(self):
        return self.content[:20]

    def content_to_markdown(self):
        return self.content
