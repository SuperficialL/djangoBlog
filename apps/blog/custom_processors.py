from apps.blog.models import Category, Tag, Article, SiteInfo, Link, Notice, Total


def global_variable(request):
    """全局通用信息"""
    categories = Category.objects.all()
    recommend = Article.objects.filter(tui__id=2)[:6]
    tags = Tag.objects.all()
    site_info = SiteInfo.objects.all().first()
    hot = Article.objects.all().order_by('views')[:10]
    links = Link.objects.all()
    notices = Notice.objects.all().order_by('-created_time')[:4]
    # 获取最新的4条消息通知
    total = Total.objects.filter(id=1)[0]
    return locals()
