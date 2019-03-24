from blog.models import Category, Tag, Article, SiteInfo, Link


def global_variable(request):
    """全局通用信息"""
    categories = Category.objects.all()
    recommend = Article.objects.filter(tui__id=2)[:6]
    tags = Tag.objects.all()
    site_info = SiteInfo.objects.all().first()
    hot = Article.objects.all().order_by('views')[:10]
    links = Link.objects.all()
    return locals()
