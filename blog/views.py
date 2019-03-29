from django.shortcuts import render
from django.http import Http404
from blog.models import Category, Banner, Article, Tag, Link
from comment.models import Comment
from .utils import get_pages


def index(request):
    """首页"""
    banner = Banner.objects.filter(is_active=True)[0:4]
    tui = Article.objects.filter(tui__id=1)[:3]
    article_list = Article.objects.all().order_by('-id')
    paginator, pages = get_pages(request, article_list)
    return render(request, 'index.html', locals())


def category(request, pk):
    """列表页"""
    article_list = Article.objects.filter(category_id=pk)
    category_name = Category.objects.get(id=pk)
    paginator, pages = get_pages(request, article_list)
    return render(request, 'category.html', locals())


def detail(request, pk):
    """内容页"""
    try:
        article = Article.objects.get(id=pk)
    except ValueError:
        raise Http404
    article.viewed()
    comment_list = Comment.objects.filter(article_id=pk)
    hot = Article.objects.all().order_by('?')[:10]
    return render(request, 'detail.html', locals())


def tag(request, tag):
    """标签页"""
    article_list = Article.objects.filter(tags__name=tag)
    tag_name = Tag.objects.get(name=tag)
    paginator, pages = get_pages(request, article_list)
    return render(request, 'tags.html', locals())


def search(request):
    """搜索页"""
    try:
        keyword = request.GET.get('search')
        if not keyword:
            return index(request)
        article_list = Article.objects.filter(title__contains=keyword)
        paginator, pages = get_pages(request, article_list)
    except Exception:
        raise Http404
    return render(request, 'search.html', locals())


def about(request):
    """关于我们"""
    return render(request, 'about.html', locals())
