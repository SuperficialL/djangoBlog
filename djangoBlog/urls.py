"""personalBlog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve
from django.conf.urls.static import static
from django.conf import settings
from blog import views
from django.contrib.sitemaps.views import sitemap
from .sitemaps import StaticViewSitemap, ArticleSiteMap, CategorySiteMap, TagSiteMap
from .feeds import Feeds

sitemaps = {
    'static': StaticViewSitemap,
    'blog': ArticleSiteMap,
    'Category': CategorySiteMap,
    'Tag': TagSiteMap,
}

urlpatterns = [
                  re_path(r'^admin/', admin.site.urls),
                  path(r'', include('apps.blog.urls', namespace='blog')),
                  re_path(r'^comment/', include('apps.comments.urls', namespace='comment')),
                  path('mdeditor/', include('mdeditor.urls')),
                  path('download/', views.download, name='download'),
                  re_path(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps},
                          name='django.contrib.sitemaps.views.sitemap'),
                  re_path(r'^feed/$', Feeds()),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
