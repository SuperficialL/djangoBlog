from django.core.paginator import Paginator
from django.utils import timezone
from apps.accounts.models import VisitNumber, DayNumber, UserIP
from .ip_to_address import ip_to_addr
import re


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
    visit_obj = VisitNumber.objects.first()
    if visit_obj:
        # 判断对象是否存在
        visit_obj.update()
    else:
        visit_obj = VisitNumber()
        visit_obj.count = 1
        visit_obj.save()

    ip, country = ip_to_addr(request)
    # 获取ip地址
    user_obj = UserIP.objects.filter(ip=ip)
    if user_obj:
        # 判断ip是否存在数据库
        user_obj.first().viewed()
        user_obj.update(end_point=end_point)
    else:
        user_obj = UserIP()
        user_obj.ip = ip
        user_obj.end_point = end_point
        user_obj.count = 1
        try:
            user_obj.ip_addr = country
        except BaseException as e:
            print(e)
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


def get_user_agent(request):
    """检测浏览器类型"""
    agent = request.META.get('HTTP_USER_AGENT', None)
    pattern = r'[\w]+ [\d]+\.[\d]+'
    user_agent = agent.lower().replace('/', ' ')
    browser = re.findall(pattern, user_agent)
    if 'safari' in browser[-1] and 'chrome' in browser[-2]:
        browser = browser[-2]
    else:
        browser = browser[-1]
    if 'qqbrowser' in browser:
        """QQ浏览器"""
        browser = browser.replace('qqb', 'QQB')
    else:
        """非QQ浏览器"""
        browser = browser.capitalize()
    print(browser, 'browser')
    return browser
