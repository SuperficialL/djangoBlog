from django.contrib import admin
from apps.accounts.models import DayNumber, UserIP, VisitNumber


# Register your models here.

@admin.register(DayNumber)
class DayNumberAdmin(admin.ModelAdmin):
    list_display = ('pk', 'day', 'count')
    list_filter = ('day', 'count')


@admin.register(UserIP)
class UserIPAdmin(admin.ModelAdmin):
    list_display = ('pk', 'ip', 'ip_addr', 'end_point', 'count', 'created_time')
    list_filter = ('ip_addr',)


@admin.register(VisitNumber)
class VisitNumberAdmin(admin.ModelAdmin):
    list_display = ('pk', 'count')
    list_filter = ('count',)
