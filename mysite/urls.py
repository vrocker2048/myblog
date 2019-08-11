"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from app01 import views
from django.conf import settings
from django.conf.urls import url, include
from DjangoUeditor import urls as djud_urls
from django.conf.urls.static import static
from mysite.settings import STATIC_ROOT
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', views.new_list, name='index' ),
    path('posts/', views.post_list),
    url(r'ueditor/', include(djud_urls)),
    url(r'^blog/(?P<bid>[0-9]+)/$', views.blog_detail, name='blog_detail'),
    # url(r'^category/(?P<categoryID>[\d]+)', views.category, name = 'category'),
    url(r'^tags/$', views.category, name='category'),
    url(r'^tags/(?P<tid>[0-9]+)/$', views.category_list),
    url(r'^projects/$', views.projects, name='projects'),
    url(r'^about/$', views.about, name='about'),
    # url(r'^static/(?P<path>.*)$','django.views.static.serve', {'document_root':settings.STATIC_ROOT}),


]
# handler404 = views.page_not_found
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

