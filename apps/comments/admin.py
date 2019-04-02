from django.contrib import admin
from .models import Comment
from apps.blog.models import Total


# Register your models here.

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'url', 'article_id', 'created_time', 'parent_id', 'browser', 'ip_addr')

    def save_model(self, request, obj, form, change):
        """统计博客数目"""
        obj.save()
        comment_nums = Comment.objects.count()
        print(comment_nums, 'comment_nums')
        total = Total.objects.get(id=1)
        total.comment_nums = comment_nums
        total.save()

    def delete_model(self, request, obj):
        obj.delete()
        comment_nums = Comment.objects.count()
        print(comment_nums, 'comment_nums')
        print(comment_nums, 'comment_nums')
        total = Total.objects.get(id=1)
        total.comment_nums = comment_nums
        total.save()
