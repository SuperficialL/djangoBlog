from django.shortcuts import render
from django.http import Http404, StreamingHttpResponse
from django.conf import settings
from apps.blog.models import Category, Banner, Article, Tag
from apps.comments.models import Comment
from utils.utils import get_pages, total_info


def index(request):
    """首页"""
    total_info(request)
    banner = Banner.objects.filter(is_active=True)[0:4]
    tui = Article.objects.filter(tui__id=1)[:3]
    article_list = Article.objects.all().order_by('-id')
    paginator, pages = get_pages(request, article_list)
    return render(request, 'index.html', locals())


def category(request, pk):
    """列表页"""
    total_info(request)
    article_list = Article.objects.filter(category_id=pk)
    category_name = Category.objects.get(id=pk)
    paginator, pages = get_pages(request, article_list)
    return render(request, 'category.html', locals())


def detail(request, pk):
    """内容页"""
    total_info(request)
    try:
        article = Article.objects.get(id=pk)
    except ValueError:
        raise Http404
    article.viewed()
    comment_list = Comment.objects.filter(article_id=pk)
    hot = Article.objects.all().order_by('?')[:10]
    return render(request, 'detail.html', locals())


def tag(request, pk):
    """标签页"""
    total_info(request)
    try:
        article_list = Article.objects.get(tags=pk)
    except ValueError:
        raise Http404
    tag_name = Tag.objects.get(name=tag)
    paginator, pages = get_pages(request, article_list)
    return render(request, 'tags.html', locals())


def search(request):
    """搜索页"""
    total_info(request)
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


def download(request):
    """下载数据"""

    def file_download(filename):
        with open(filename) as f:
            while True:
                c = f.read(512)
                if c:
                    yield c
                else:
                    break

    # filename = settings.BASE_DIR + '/data.json'
    filename = 'data.json'
    response = StreamingHttpResponse(file_download(filename))
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename=%s' % filename
    return response
