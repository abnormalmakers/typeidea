from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from .models import Tag, Post, Category
from config.models import Sidebar

# Create your views here.
# def post_list(request,category_id=None,tag_id=None):
#     tag=None
#     category=None
#
#     if tag_id:
#         try:
#             tag=Tag.objects.get(id=tag_id)
#         except Tag.DoseNotExsit:
#             post_list=[]
#         else:
#             post_list=tag.post_set.filter(status=Post.STATUS_NORMAL)
#     else:
#         post_list=Post.objects.filter(status=Post.STATUS_NORMAL)
#         if category_id:
#             try:
#                 category=Category.objects.get(id=category_id)
#             except Category.DoseNotExist:
#                 category=None
#             else:
#                 post_list=post_list.filter(category_id=category_id)
#
#             post_list=Post.objects.filter(category_id=category_id)
#
#     context={
#         'category':category,
#         'tag':tag,
#         'post_list':post_list
#     }
#
#     return render(request,'blog/list.html',context=context)

# def post_list(request,category_id=None,tag_id=None):
#     tag=None
#     category=None
#
#     if tag_id:
#         post_list,tag=Post.get_by_tag(tag_id)
#     elif category_id:
#         post_list,category=Post.get_by_category(category_id)
#     else:
#         post_list=Post.latest_posts()
#
#     context={
#         'category':category,
#         'tag':tag,
#         'post_list':post_list,
#         'sidebars':Sidebar.get_all()
#     }
#     context.update(Category.get_navs())
#     return render(request,'blog/list.html',context=context)

# def post_detail(request,post_id=None):
#     try:
#         post=Post.objects.get(id=post_id)
#     except Post.DoesNotExist:
#         post=None
#     return render(request,'blog/detail.html',context={'post':post})


# 增加通用数据，实现get_context_data,首页继承此类获取数据
class CommonViewMixin:
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context.update({
            'sidebars':Sidebar.get_all()
        })
        context.update(Category.get_navs())
        context.update({
            'tags':Tag.get_tag_all()
        })
        return context


class IndexView(CommonViewMixin,ListView):
    queryset=Post.latest_posts()
    paginate_by = 1
    context_object_name = 'post_list'
    template_name = 'blog/list.html'

    # def get_queryset(self):
    #     posts=Post.latest_posts()
    #     return posts


class CategoryView(IndexView):
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        category_id=self.kwargs.get('category_id')
        category=get_object_or_404(Category,pk=category_id)
        context.update({
            'category':category
        })
        return context

    def get_queryset(self):
        """重写get_queryset，根据分类过滤"""
        queryset=super().get_queryset()
        category_id=self.kwargs.get('category_id')
        return queryset.filter(category_id=category_id)


class TagView(IndexView):
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        tag_id=self.kwargs.get('tag_id')
        tag=get_object_or_404(Tag,pk=tag_id)
        context.update({
            'tag':tag
        })
        return context

    def get_queryset(self):
        """重写get_queryset，根据标签过滤"""
        queryset=super().get_queryset()
        tag_id=self.kwargs.get('tag_id')
        qs=queryset.filter(tag__id=tag_id)
        return qs


class PostDetailView(CommonViewMixin,DetailView):
    template_name = 'blog/detail.html'
    queryset = Post.latest_posts()
    context_object_name = 'post'
    pk_url_kwarg = 'post_id'

