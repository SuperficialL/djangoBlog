from django.shortcuts import render
from blog.models import Category, Banner, Article, Tag, Link
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def index(request):
    """首页"""
    banner = Banner.objects.filter(is_active=True)[0:4]
    tui = Article.objects.filter(tui__id=1)[:3]
    article_list = Article.objects.all().order_by('-id')[0:10]
    hot = Article.objects.all().order_by('views')[:10]
    return render(request, 'index.html', locals())


def category(request, pk):
    """列表页"""
    article_list = Article.objects.filter(category_id=pk)
    category_name = Category.objects.get(id=pk)
    page = request.GET.get('page')
    paginator = Paginator(article_list, 5)
    try:
        list = paginator.page(page)
        # 获取当前页码的记录
    except PageNotAnInteger:
        list = paginator.page(1)
        # 如果用户输入的页码不是整数时,显示第1页的内容
    except EmptyPage:
        list = paginator.page(paginator.num_pages)
        # 如果用户输入的页数不在系统的页码列表中时,显示最后一页的内容
    return render(request, 'category.html', locals())


def detail(request, pk):
    # 内容页
    article = Article.objects.get(id=pk)
    article.viewed()
    hot = Article.objects.all().order_by('?')[:10]
    return render(request, 'detail.html', locals())


def tag(request, tag):
    # 标签页
    list = Article.objects.filter(tags__name=tag)
    tname = Tag.objects.get(name=tag)
    page = request.GET.get('page')
    paginator = Paginator(list, 5)
    try:
        list = paginator.page(page)  # 获取当前页码的记录
    except PageNotAnInteger:
        list = paginator.page(1)  # 如果用户输入的页码不是整数时,显示第1页的内容
    except EmptyPage:
        list = paginator.page(paginator.num_pages)  # 如果用户输入的页数不在系统的页码列表中时,显示最后一页的内容
    return render(request, 'tags.html', locals())


def search(request):
    # 搜索页
    ss = request.GET.get('search')
    list = Article.objects.filter(title__contains=ss)
    page = request.GET.get('page')
    paginator = Paginator(list, 10)
    try:
        list = paginator.page(page)
        # 获取当前页码的记录
    except PageNotAnInteger:
        list = paginator.page(1)
        # 如果用户输入的页码不是整数时,显示第1页的内容
    except EmptyPage:
        list = paginator.page(paginator.num_pages)
        # 如果用户输入的页数不在系统的页码列表中时,显示最后一页的内容
    return render(request, 'search.html', locals())


def about(request):
    # 关于我们
    return render(request, 'page.html', locals())
