from django.shortcuts import render
from blog.models import Category, Banner, Article, Tag, Link, Comment
from .utils import get_page


def index(request):
    """首页"""
    banner = Banner.objects.filter(is_active=True)[0:4]
    tui = Article.objects.filter(tui__id=1)[:3]
    article_list = Article.objects.all().order_by('-id')
    paginator, article_list = get_page(request, article_list)
    return render(request, 'index.html', locals())


def category(request, pk):
    """列表页"""
    article_list = Article.objects.filter(category_id=pk)
    category_name = Category.objects.get(id=pk)
    paginator, article_list = get_page(request, article_list)
    return render(request, 'category.html', locals())


def detail(request, pk):
    # 内容页
    article = Article.objects.get(id=pk)
    article.viewed()
    comment_list = Comment.objects.filter(article_id=pk)
    hot = Article.objects.all().order_by('?')[:10]

    return render(request, 'detail.html', locals())


def tag(request, tag):
    # 标签页
    article_list = Article.objects.filter(tags__name=tag)
    tag_name = Tag.objects.get(name=tag)
    # 获取当前页码，如果没有参数，则默认第一页
    paginator, article_list = get_page(request, article_list)
    return render(request, 'tags.html', locals())


def search(request):
    # 搜索页
    ss = request.GET.get('search')
    article_list = Article.objects.filter(title__contains=ss)
    # 获取当前页码，如果没有参数，则默认第一页
    paginator, article_list = get_page(request, article_list)
    return render(request, 'search.html', locals())


def about(request):
    # 关于我们
    return render(request, 'page.html', locals())
