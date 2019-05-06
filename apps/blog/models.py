from django.db import models
from django.urls import reverse
from django.conf import settings
from django.template.defaultfilters import slugify
from mdeditor import fields as md_models
import markdown


class Navigation(models.Model):
    """导航分类"""
    name = models.CharField('导航名',
                            unique=True,
                            max_length=100)
    index = models.IntegerField(default=999,
                                verbose_name='分类排序')
    slug = models.SlugField('网页路径')

    def get_absolute_url(self):
        """返回该对象的绝对路径"""
        return reverse('blog:category',
                       kwargs={
                           'slug': self.slug,
                           'nav_slug': ''
                       })

    def save(self, *args, **kwargs):
        if not (self.id or not self.slug):
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = '导航分类'
        verbose_name_plural = verbose_name
        ordering = ['index', 'pk']

    def __str__(self):
        return self.name


class Category(models.Model):
    """文章分类"""
    name = models.CharField(verbose_name='分类名',
                            unique=True,
                            max_length=50)
    navigation = models.ForeignKey(Navigation,
                                   on_delete=models.CASCADE,
                                   verbose_name='分类导航',
                                   null=True)
    slug = models.SlugField('网页路径')

    def get_absolute_url(self):
        """返回该对象的绝对路径"""
        return reverse('blog:category',
                       kwargs={
                           'slug': self.slug,
                           'nav_slug': self.navigation.slug
                       })

    def save(self, *args, **kwargs):
        if not (self.id or not self.slug):
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_article_list(self):
        """获取该分类下所有文章"""
        return Article.objects.filter(category=self)

    class Meta:
        verbose_name = '文章分类'
        verbose_name_plural = verbose_name
        ordering = ['id']

    def __str__(self):
        return self.name


class Tag(models.Model):
    """文章标签"""
    name = models.CharField('文章标签',
                            unique=True,
                            max_length=100)
    slug = models.SlugField('网页路径')

    def get_absolute_url(self):
        """返回该对象的绝对路径"""
        return reverse('blog:tag', kwargs={'tag_name': self.name})

    def get_article_list(self):
        """返回当前标签下所有发表的文章列表"""
        return Article.objects.filter(tags=self)

    def save(self, *args, **kwargs):
        if not (self.id or not self.slug):
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

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
    STATUS_CHOICES = (
        ('d', '草稿'),
        ('p', '发表')
    )
    IMG_LINK = '/static/images/python.jpg'
    title = models.CharField('标题',
                             unique=True,
                             max_length=70)
    summary = models.TextField('文章摘要',
                               max_length=200,
                               blank=True)
    body = md_models.MDTextField('内容', blank=True)
    status = models.CharField('状态',
                              choices=STATUS_CHOICES,
                              max_length=1,
                              default='p')
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.DO_NOTHING,
                               verbose_name='作者')
    category = models.ForeignKey(Category,
                                 verbose_name='分类',
                                 on_delete=models.CASCADE)
    img = models.ImageField(upload_to='article_img/%Y/%m/%d/',
                            verbose_name='文章图片',
                            default=IMG_LINK)
    # 使用外键关联分类表与分类是一对多关系
    tags = models.ManyToManyField(Tag,
                                  verbose_name='标签',
                                  blank=True)
    # 使用外键关联标签表与标签是多对多关系
    format_content = models.TextField(verbose_name='格式化内容',
                                      blank=True)
    views = models.PositiveIntegerField('阅读量',
                                        default=0)
    loves = models.IntegerField('喜爱量', default=0)
    tui = models.ForeignKey(Tui,
                            on_delete=models.DO_NOTHING,
                            verbose_name='推荐位',
                            blank=True,
                            null=True)
    created_time = models.DateTimeField(verbose_name='发布时间',
                                        auto_now_add=True)
    updated_time = models.DateTimeField(verbose_name='修改时间',
                                        auto_now=True)

    def save(self, *args, **kwargs):
        self.format_content = markdown.markdown(self.body.replace("\r\n", '  \n'),
                                                extensions=[
                                                    'markdown.extensions.extra',
                                                    'markdown.extensions.codehilite',
                                                    'markdown.extensions.toc',
                                                ])
        self.summary = self.format_content[:200]
        super(Article, self).save(*args, **kwargs)

    def body_to_markdown(self):
        return markdown.markdown(self.body, extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
        ])

    def update_views(self):
        # 访问量加一
        self.views += 1
        self.save(update_fields=['views'])

    def next_article(self):
        # 下一篇
        return Article.objects.filter(id__gt=self.id, status='p').order_by('id').first()

    def prev_article(self):
        # 前一篇
        return Article.objects.filter(id__lt=self.id, status='p').order_by('pk').last()

    def get_absolute_url(self):
        """返回该对象的绝对路径"""
        return reverse('blog:detail', kwargs={
            'article_id': self.id,
            'year': self.created_time.year,
            'month': self.created_time.month,
            'day': self.created_time.day
        })

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name
        ordering = ['id']

    def __str__(self):
        return str(self.title)


class Banner(models.Model):
    """轮播图"""
    title = models.CharField('标题', max_length=50, blank=True)
    number = models.IntegerField('编号',
                                 help_text='编号决定图片播放的顺序，图片建议不要多于5张')
    img = models.ImageField('轮播图', upload_to='banner/')
    link_url = models.URLField('图片链接', max_length=100,
                               null=True, blank=True)
    is_active = models.BooleanField('是否激活', default=False)

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = '轮播图'
        verbose_name_plural = verbose_name
        ordering = ['number', '-id']


class FriendLink(models.Model):
    """友情链接"""
    name = models.CharField(verbose_name='链接名称', max_length=40)
    link_url = models.URLField(verbose_name='网址',
                               max_length=100,
                               help_text='请填写http或https开头的完整形式地址')
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
    is_active = models.BooleanField('是否激活',
                                    default=False)
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
