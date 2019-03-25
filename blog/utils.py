from django.core.paginator import Paginator


def get_pages(request, list):
    """分页"""
    page = request.GET.get('page', 1)
    paginator = Paginator(list, 5)
    pages = paginator.get_page(page)
    # get_page() 获取当前页码的记录,并对页码进行判断
    return paginator, pages
