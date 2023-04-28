"""personal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from django.urls import include
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve as mediaserve
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.views.generic.base import RedirectView

from django.contrib.staticfiles.storage import staticfiles_storage

from django.contrib.sitemaps.views import sitemap
from blogs.models import Post
from blogs.sitemaps import PostSitemap

admin.site.site_header = 'Admin Panel'
admin.site.index_title = 'App Administration'

sitemaps = {
    'posts': PostSitemap,
}


urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include('portfolio.urls')),
        path('blogs/', include('blogs.urls')),
        path('works/', include('works.urls')),
        path('summernote/', include('django_summernote.urls')),
        path("ads.txt", RedirectView.as_view(url=staticfiles_storage.url("ads.txt")),),

        path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, 
             name='django.contrib.sitemaps.views.sitemap'),
        path('mdeditor/', include('mdeditor.urls')),
]

urlpatterns.append(url(f'^{settings.MEDIA_URL.lstrip("/")}(?P<path>.*)$',
                       mediaserve, {'document_root': settings.MEDIA_ROOT}))

# urlpatterns.append(url(r"^static/(?P<path>.*)$", 'django.views.static.serve', {'document_root':
#                       settings.STATIC_ROOT}))

urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
