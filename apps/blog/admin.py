from django.contrib import admin
from .models import Banner, Navigation, Category, Tag, Tui, Article, FriendLink, SiteInfo, Total, Notice


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'tui', 'author', 'views', 'created_time', 'status')
    list_filter = ('tui', 'author', 'created_time', 'status')
    # 文章列表里显示想要显示的字段
    list_per_page = 50
    # 满50条数据就自动分页
    ordering = ('-created_time',)
    # 后台数据列表排序方式
    list_display_links = ('id', 'title')

    # 设置哪些字段可以点击进入编辑界面


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'img', 'link_url', 'is_active')
    list_filter = ('title', 'img', 'link_url', 'is_active')


@admin.register(Navigation)
class NavigationAdmin(admin.ModelAdmin):
    list_display = ('id', 'index', 'name', 'slug')
    list_filter = ('name', 'slug')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_filter = ('name',)

    def save_model(self, request, obj, form, change):
        """统计博客数目"""
        obj.save()
        category_nums = Category.objects.count()
        print(category_nums, 'category_nums')
        total = Total.objects.get(id=1)
        total.category_nums = category_nums
        total.save()

    def delete_model(self, request, obj):
        obj.delete()
        category_nums = Category.objects.count()
        print(category_nums, 'category_nums')
        total = Total.objects.get(id=1)
        total.category_nums = category_nums
        total.save()


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_filter = ('name',)

    def save_model(self, request, obj, form, change):
        """统计博客数目"""
        obj.save()
        tag_nums = Tag.objects.count()
        print(tag_nums, 'tag_nums')
        total = Total.objects.get(id=1)
        total.tag_nums = tag_nums
        total.save()

    def delete_model(self, request, obj):
        obj.delete()
        tag_nums = Tag.objects.count()
        print(tag_nums, 'tag_nums')
        total = Total.objects.get(id=1)
        total.tag_nums = tag_nums
        total.save()


@admin.register(Tui)
class TuiAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_filter = ('name',)


@admin.register(FriendLink)
class FriendLinkAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'link_url')
    list_filter = ('name', 'link_url')


@admin.register(SiteInfo)
class SiteInfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'site_name', 'keywords', 'description', 'copyright', 'code')
    list_filter = ('site_name', 'keywords', 'description', 'copyright', 'code')


@admin.register(Notice)
class NoticeAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'created_time')


@admin.register(Total)
class TotalAdmin(admin.ModelAdmin):
    list_display = ('id', 'article_nums', 'comment_nums', 'tag_nums', 'category_nums', 'visit_nums')
