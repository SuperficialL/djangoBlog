from blog.models import Navigation, Tag, Article, SiteInfo, FriendLink, Notice, Total


def global_variable(request):
    """全局通用信息"""
    recommend = Article.objects.filter(status='p', tui__id=2)[:6]
    tags = Tag.objects.all()
    site_info = SiteInfo.objects.all().first()
    links = FriendLink.objects.all()
    notices = Notice.objects.all().order_by('-created_time')[:4]
    # 获取最新的4条消息通知
    total = Total.objects.filter(id=1)[0]
    return locals()
