#!/usr/bin/python3
# encoding: utf-8
# @Time : 2019/3/3121:29
# @Author Superficial
# @File ip_to_address.py
# @Software PyCharm

from django.conf import settings
import geoip2.database


def ip_to_addr(request):
    """将IP转换成现实中的地理位置
    country = 国家
    province = 省
    city = 城市
    """
    if 'HTTP_X_FORWARDED_FOR' in request.META:
        # 获取真实IP
        ip = request.META['HTTP_X_FORWARDED_FOR']
    else:
        # 获取代理IP
        ip = request.META['REMOTE_ADDR']
    reader = geoip2.database.Reader(settings.GEOIP_PATH)
    response = reader.city(ip)
    province = ''
    city = ''
    try:
        country = response.country.names['zh-CN']
        province = response.subdivisions.most_specific.names["zh-CN"]
        city = response.city.names['zh-CN']
    except KeyError as e:
        # 没有获取到键将错误写入日志
        pass
    if country != '中国':
        return ip, country
    if province and city:
        if province == city or city in province:
            return ip, province
        return ip, '%s%s' % (province, city)
    elif province and not city:
        return ip, province
    else:
        return ip, country
