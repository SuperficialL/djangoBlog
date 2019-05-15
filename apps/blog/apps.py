from django.apps import AppConfig


class BlogConfig(AppConfig):
    name = 'blog'
    verbose_name = '博客'

    def ready(self):
        """注册信号"""
        from .signals import article_save
