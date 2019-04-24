from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from mdeditor import fields as md_models
import markdown
from django.utils.timezone import now

User = get_user_model()


class Navigation(models.Model):
    """导航分类"""
    name = models.CharField('导航名',
                            max_length=100)
    index = models.IntegerField(default=999,
                                verbose_name='分类排序')

    class Meta:
        verbose_name = '导航分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Category(models.Model):
    """文章分类"""
    name = models.CharField(verbose_name='分类名',
                            max_length=50)
    navigation = models.ForeignKey(Navigation,
                                   on_delete=models.CASCADE,
                                   verbose_name='分类导航',
                                   null=True)
    created_time = models.DateTimeField(verbose_name='发布时间',
                                        auto_now_add=True,
                                        null=True, blank=True)

    modified_time = models.DateTimeField(verbose_name='修改时间',
                                         auto_now=True,
                                         null=True, blank=True)

    def get_absolute_url(self):
        """返回该对象的绝对路径"""
        return reverse('blog:category', self.id)

    class Meta:
        verbose_name = '文章分类'
        verbose_name_plural = verbose_name
        ordering = ['id']

    def __str__(self):
        return self.name


class Tag(models.Model):
    """文章标签"""
    name = models.CharField('文章标签',
                            max_length=100)
    created_time = models.DateTimeField(verbose_name='发布时间',
                                        auto_now_add=True,
                                        null=True, blank=True)

    modified_time = models.DateTimeField(verbose_name='修改时间',
                                         auto_now=True,
                                         null=True,blank=True)

    def get_absolute_url(self):
        """返回该对象的绝对路径"""
        return reverse('blog:tags', self.id)

    class Meta:
        verbose_name = '文章标签'
        verbose_name_plural = verbose_name
        ordering = ['id']

    def __str__(self):
        return self.name


class Tui(models.Model):
    """推荐位"""
    name = models.CharField('推荐位', max_length=100)

    class Meta:
        verbose_name = '推荐位'
        verbose_name_plural = verbose_name
        ordering = ['id']

    def __str__(self):
        return self.name


class Article(models.Model):
    """文章"""
    IMG_LINK = '/static/images/python.jpg'
    title = models.CharField(verbose_name='标题',
                             max_length=70)
    excerpt = models.TextField(verbose_name='摘要',
                               max_length=200)
    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE,
                                 verbose_name='分类',
                                 null=True)
    # 使用外键关联分类表与分类是一对多关系
    tags = models.ManyToManyField(Tag, verbose_name='标签', blank=True)
    # 使用外键关联标签表与标签是多对多关系
    img = models.ImageField(upload_to='article_img/%Y/%m/%d/',
                            verbose_name='文章图片', default=IMG_LINK)
    body = md_models.MDTextField(verbose_name='内容', blank=True)
    format_content = models.TextField(verbose_name='格式化内容',
                                      blank=True)
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             verbose_name='作者')
    views = models.PositiveIntegerField('阅读量',
                                        default=0)
    tui = models.ForeignKey(Tui,
                            on_delete=models.DO_NOTHING,
                            verbose_name='推荐位',
                            blank=True,
                            null=True)
    created_time = models.DateTimeField(verbose_name='发布时间',
                                        auto_now_add=True)
    modified_time = models.DateTimeField(verbose_name='修改时间',
                                         auto_now=True)

    def save(self, *args, **kwargs):
        self.format_content = markdown.markdown(self.body.replace("\r\n", '  \n'),
                                                extensions=[
                                                    'markdown.extensions.extra',
                                                    'markdown.extensions.codehilite',
                                                    'markdown.extensions.toc',
                                                ])
        super(Article, self).save(*args, **kwargs)

    def viewed(self):
        # 访问量加一
        self.views += 1
        self.save(update_fields=['views'])

    def next_article(self):
        # 下一篇
        return Article.objects.filter(id__gt=self.id).order_by('id').first()

    def prev_article(self):
        # 前一篇
        return Article.objects.filter(id__lt=self.id).order_by('id').last()

    def get_absolute_url(self):
        """返回该对象的绝对路径"""
        return reverse('blog:detail', self.id)

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name
        ordering = ['id']

    def __str__(self):
        return self.title


class Banner(models.Model):
    """轮播图"""
    text_info = models.CharField('标题', max_length=50, default='')
    img = models.ImageField('轮播图', upload_to='banner/')
    link_url = models.URLField('图片链接', max_length=100)
    is_active = models.BooleanField('是否是active', default=False)

    def __str__(self):
        return self.text_info

    class Meta:
        verbose_name = '轮播图'
        verbose_name_plural = verbose_name
        ordering = ['id']


class Link(models.Model):
    """友情链接"""
    name = models.CharField(verbose_name='链接名称', max_length=40)
    link_url = models.URLField(verbose_name='网址', max_length=100)
    is_active = models.BooleanField('是否有效', default=True)
    is_show = models.BooleanField('是否首页展示', default=False)

    def active_to_false(self):
        self.is_active = False
        self.save(update_fields=['is_active'])

    def show_to_false(self):
        self.is_show = True
        self.save(update_fields=['is_show'])

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '友情链接'
        verbose_name_plural = verbose_name
        ordering = ['id']


class SiteInfo(models.Model):
    """站点信息"""
    site_name = models.CharField(verbose_name='站点名称',
                                 max_length=40)
    keywords = models.CharField(verbose_name='站点关键字',
                                max_length=200)
    description = models.TextField(verbose_name='站点描述')
    copyright = models.CharField(verbose_name='站点版权',
                                 max_length=200)
    code = models.CharField(verbose_name='备案号',
                            max_length=200)

    def __str__(self):
        return self.site_name

    class Meta:
        verbose_name = '站点信息'
        verbose_name_plural = verbose_name
        ordering = ['id']


class Notice(models.Model):
    """公告通知"""
    text = models.CharField(verbose_name='信息',
                            max_length=300)
    # is_active = models.BooleanField(verbose_name='是否激活',
    #                                 default=False)
    created_time = models.DateTimeField(verbose_name='创建时间',
                                        auto_now_add=True)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = '博客事件信息'
        verbose_name_plural = verbose_name
        ordering = ['created_time']


class Total(models.Model):
    """统计文章数,分类数,标签数,评论数,访问总数"""
    article_nums = models.IntegerField(verbose_name='文章数',
                                       default=0)
    category_nums = models.IntegerField(verbose_name='分类数',
                                        default=0)
    comment_nums = models.IntegerField(verbose_name='评论数',
                                       default=0)
    tag_nums = models.IntegerField(verbose_name='标签数',
                                   default=0)
    visit_nums = models.IntegerField(verbose_name='访问总数',
                                     default=0)

    def __str__(self):
        return '文章数:%s分类数%s标签数%s评论数%s访问总数%s' % \
               (self.article_nums, self.category_nums, self.tag_nums, self.comment_nums, self.visit_nums)

    class Meta:
        verbose_name = '博客统计信息'
        verbose_name_plural = verbose_name
        ordering = ['id']
