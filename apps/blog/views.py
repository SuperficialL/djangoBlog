from django.shortcuts import render
from django.http import Http404, StreamingHttpResponse
from django.conf import settings
from utils.utils import get_pages, total_info
from django.views import generic
from django.shortcuts import get_list_or_404, get_object_or_404
import markdown
import time
from blog.models import Category, Banner, Article, Tag, Navigation
from comments.models import Comment
import logging

logger = logging.getLogger(__name__)


class IndexView(generic.ListView):
    """列表视图,重用首页,分类,标签,归档"""
    # 数据库模型
    model = Article
    # 指定模板渲染,这里我们用指定,我重用该View用于tag,category,index,archive
    template_name = 'index.html'
    # 指定模板中使用的变量
    context_object_name = 'article_list'
    # 分页
    paginate_by = 10

    def get_queryset(self):
        return super(IndexView, self).get_queryset().filter(status='p')


class CategoryView(generic.ListView):
    model = Article
    template_name = 'category.html'
    context_object_name = 'article_list'
    paginate_by = 10

    def get_queryset(self, **kwargs):
        queryset = super(CategoryView, self).get_queryset().filter(status='p')
        self.nav_slug = self.kwargs.get('nav_slug', '')

        # 文章分类
        slug = self.kwargs.get('slug', '')
        if self.nav_slug:
            big = get_object_or_404(Navigation, slug=self.nav_slug)
            queryset = queryset.filter(category__navigation=big)

            if slug:
                slu = get_object_or_404(Category, slug=slug)
                queryset = queryset.filter(category=slu)
        return queryset

    def get_context_data(self, **kwargs):
        context_data = super(CategoryView, self).get_context_data()
        slug = self.kwargs.get('slug', '')
        if slug:
            category = get_object_or_404(Category, slug=self.kwargs.get('slug'))
        else:
            category = get_object_or_404(Navigation, slug=self.kwargs.get('nav_slug'))
        context_data['category'] = category
        return context_data


class TagView(generic.ListView):
    model = Article
    template_name = 'tags.html'
    context_object_name = 'article_list'
    paginate_by = 10

    def get_queryset(self, **kwargs):
        queryset = super(TagView, self).get_queryset().filter(status='p')
        tag_name = self.kwargs.get('tag_name', 0)
        if tag_name:
            tags = get_object_or_404(Tag, name=tag_name)
            queryset = queryset.filter(tags=tags)
        return queryset

    def get_context_data(self, **kwargs):
        context_data = super(TagView, self).get_context_data()
        context_data['tag_name'] = get_object_or_404(Tag, name=self.kwargs.get('tag_name'))
        return context_data


class ArchiveView(generic.ListView):
    model = Article
    template_name = 'archive.html'
    context_object_name = 'article_list'
    paginate_by = 200


class DetailView(generic.DetailView):
    """
        Django有基于类的视图DetailView,用于显示一个对象的详情页，我们继承它
    """
    # 获取数据库中的文章列表
    model = Article
    # template_name属性用于指定使用哪个模板进行渲染
    pk_url_kwarg = 'article_id'
    template_name = 'detail.html'
    # context_object_name属性用于给上下文变量取名（在模板中使用该名字）
    context_object_name = 'article'

    def get_object(self, queryset=None):
        obj = super(DetailView, self).get_object()
        # 设置浏览量增加时间判断,同一篇文章两次浏览超过半小时才重新统计阅览量,作者浏览忽略
        obj.update_views()
        self.object = obj
        return obj

    def get_context_data(self, **kwargs):
        article_id = int(self.kwargs[self.pk_url_kwarg])
        kwargs['next_article'] = self.object.next_article
        kwargs['prev_article'] = self.object.prev_article
        return super(DetailView, self).get_context_data(**kwargs)


def search(request):
    """搜索页"""
    total_info(request)
    try:
        keyword = request.GET.get('search')
        if not keyword:
            return IndexView()
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
