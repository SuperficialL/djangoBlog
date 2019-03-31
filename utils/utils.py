from django.core.paginator import Paginator
from django.utils import timezone
from apps.accounts.models import VisitNumber, DayNumber, UserIP


def get_pages(request, list):
    """分页"""
    page = request.GET.get('page', 1)
    paginator = Paginator(list, 5)
    pages = paginator.get_page(page)
    # get_page() 获取当前页码的记录,并对页码进行判断
    return paginator, pages


def total_info(request):
    """
    统计网站访问信息
    :param request: http请求
    """
    end_point = request.META.get('PATH_INFO', '/')
    print(end_point, 'end')
    visit_obj = VisitNumber.objects.first()
    if visit_obj:
        # 判断对象是否存在
        visit_obj.update()
    else:
        visit_obj = VisitNumber()
        visit_obj.count = 1
        visit_obj.save()

    if 'HTTP_X_FORWARDED_FOR' in request.META:
        # 获取真实IP
        ip = request.META['HTTP_X_FORWARDED_FOR']
    else:
        # 获取代理IP
        ip = request.META['REMOTE_ADDR']
    user_obj = UserIP.objects.filter(ip=str(ip))
    if user_obj:
        # 判断ip是否存在数据库
        user_obj.first().viewed()
        user_obj.update(end_point=end_point)
    else:
        user_obj = UserIP()
        user_obj.ip = ip
        user_obj.end_point = end_point
        user_obj.count = 1
        user_obj.save()

    # 增加今日访问次数
    date = timezone.now().date()
    today = DayNumber.objects.filter(day=date)
    if today:
        temp = today[0]
        temp.count += 1
    else:
        temp = DayNumber()
        temp.dayTime = date
        temp.count = 1
    temp.save()
