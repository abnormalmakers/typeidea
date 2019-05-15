"""typeidea URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.sitemaps import views as sitemap_views
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter

from blog.apis import PostViewSet, CategoryViewSet, TagViewSet
from blog.rss import LatestPostFeed
from blog.sitemap import PostSitemap
from comment.views import CommentView
from typeidea.custom_site import custom_site
from config.views import LinkListView
from blog.views import IndexView, CategoryView, TagView, PostDetailView, SearchView, AuthorView
from mytest.views import MytestA,MytestB

router=DefaultRouter()
router.register(r'post',PostViewSet,base_name='api-post')
router.register(r'category',CategoryViewSet,base_name='api-category')
router.register(r'tag',TagViewSet,base_name='api-tag')

urlpatterns = [
    url(r'^super_admin/',admin.site.urls,name='super=admin'),
    url(r'^admin/', custom_site.urls,name='admin'),
]
urlpatterns +=[
    url(r'^$',IndexView.as_view(),name='index'),
    url(r'^category/(?P<category_id>\d+)/$',CategoryView.as_view(),name='category-list'),
    url(r'^tag/(?P<tag_id>\d+)/$',TagView.as_view(),name='tag-list'),
    url(r'^post/(?P<post_id>\d+).html$',PostDetailView.as_view(),name='post-detail'),
    url(r'^links/$',LinkListView.as_view(),name='links'),
    url(r'^search/$',SearchView.as_view(),name='search'),
    url(r'^author/(?P<owner_id>\d+)$',AuthorView.as_view(),name='author'),
    url(r'^comment/$',CommentView.as_view(),name='comment'),
    url(r'^rss|feed/',LatestPostFeed(),name='rss'),
    url(r'^sitemap\.xml$',sitemap_views.sitemap,{'sitemaps':{'posts':PostSitemap}}),
    url(r'^api/',include(router.urls)),
    url(r'^api/docs/',include_docs_urls(title='typeidea.apis')),
    # url(r'^api/post/',post_list,name='post-list'),
    # url(r'^api/post/',PostList.as_view(),name='post-list'),
    url(r'^mytesta',MytestA.as_view()),
    url(r'^mytestb',MytestB.as_view())
]
