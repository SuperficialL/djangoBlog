from django.db import models
from django.contrib.auth.models import User
from DjangoUeditor.models import UEditorField


class Category(models.Model):
    # 文章分类
    name = models.CharField('博客分类',
                            max_length=100)
    index = models.IntegerField(default=999,
                                verbose_name='分类排序')

    class Meta:
        verbose_name = '博客分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Tag(models.Model):
    # 文章标签
    name = models.CharField('文章标签',
                            max_length=100)

    class Meta:
        verbose_name = '文章标签'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Tui(models.Model):
    # 推荐位
    name = models.CharField('推荐位', max_length=100)

    class Meta:
        verbose_name = '推荐位'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Article(models.Model):
    # 文章
    title = models.CharField('标题', max_length=70)
    excerpt = models.TextField('摘要',
                               max_length=200,
                               blank=True)
    category = models.ForeignKey(Category,
                                 on_delete=models.DO_NOTHING,
                                 verbose_name='分类',
                                 blank=True,
                                 null=True)
    # 使用外键关联分类表与分类是一对多关系
    tags = models.ManyToManyField(Tag, verbose_name='标签', blank=True)
    # 使用外键关联标签表与标签是多对多关系
    img = models.ImageField(upload_to='article_img/%Y/%m/%d/',
                            verbose_name='文章图片',
                            blank=True,
                            null=True)
    body = UEditorField('内容',
                        width=800,
                        height=500,
                        toolbars="full",
                        imagePath="upimg/",
                        filePath="upfile/",
                        upload_settings={"imageMaxSize": 1204000},
                        settings={},
                        command=None,
                        blank=True
                        )
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
    created_time = models.DateTimeField('发布时间',
                                        auto_now_add=True)
    modified_time = models.DateTimeField('修改时间',
                                         auto_now=True)

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

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class Banner(models.Model):
    # 轮播图
    text_info = models.CharField('标题', max_length=50, default='')
    img = models.ImageField('轮播图', upload_to='banner/')
    link_url = models.URLField('图片链接', max_length=100)
    is_active = models.BooleanField('是否是active', default=False)

    def __str__(self):
        return self.text_info

    class Meta:
        verbose_name = '轮播图'
        verbose_name_plural = verbose_name


class Link(models.Model):
    # 友情链接
    name = models.CharField('链接名称', max_length=20)
    linkurl = models.URLField('网址', max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '友情链接'
        verbose_name_plural = verbose_name


class SiteInfo(models.Model):
    """站点信息"""
    site_name = models.CharField(verbose_name='站点名称',
                                 max_length=40)
    keywords = models.CharField(verbose_name='站点关键字',
                                max_length=200)
    desc = models.TextField(verbose_name='站点描述')
    copyright = models.CharField(verbose_name='站点版权',
                                 max_length=200)
    code = models.CharField(verbose_name='备案号',
                            max_length=200)

    def __str__(self):
        return self.site_name

    class Meta:
        verbose_name = '站点信息'
        verbose_name_plural = verbose_name
