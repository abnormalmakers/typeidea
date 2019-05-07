from datetime import date

from django.core.cache import cache
from django.db.models import Q,F
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


# 首页
class IndexView(CommonViewMixin,ListView):
    queryset=Post.latest_posts()
    paginate_by = 3
    context_object_name = 'post_list'
    template_name = 'blog/list.html'

    # def get_queryset(self):
    #     posts=Post.latest_posts()
    #     return posts


#分类页
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


# 标签页
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


# 文章详情页
class PostDetailView(CommonViewMixin,DetailView):
    template_name = 'blog/detail.html'
    queryset = Post.latest_posts()
    context_object_name = 'post'
    pk_url_kwarg = 'post_id'

    def get(self,request,*args,**kwargs):
        response=super().get(request,*args,**kwargs)
        self.handle_visited()
        return response

    def handle_visited(self):
        increase_pv=False
        increase_uv=False
        uid=self.request.uid

        pv_key="pv:%s:%s"%(uid,self.request.path)
        uv_key="uv:%s:%s:%s"%(uid,str(date.today()),self.request.path)

        if not cache.get(pv_key):
            increase_pv=True
            cache.set(pv_key,1,1*60)    #统计访问量，1分钟内连续刷无效


        if not cache.get(uv_key):
            increase_uv=True
            cache.set(uv_key,1,60*60*24)    #统计独立用户，一台电脑一个用户，24小时内相同客户端只计算1次

        if increase_pv and increase_uv:
            Post.objects.filter(pk=self.object.id).update(pv=F('pv')+1,uv=F('uv')+1)
        elif increase_pv:
            Post.objects.filter(pk=self.object.id).update(pv=F('pv')+1)
        elif increase_uv:
            Post.objects.filter(pk=self.object.id).update(uv=F('uv')+1)


    # def get_context_data(self,**kwargs):
    #     context=super().get_context_data(**kwargs)
    #     context.update({
    #         'comment_form':CommentForm,
    #         'comment_list':Comment.get_by_target(self.request.path)
    #     })
    #     return context


#搜索页
class SearchView(IndexView):
    def get_context_data(self):
        context=super().get_context_data()
        context.update({
            'keyword':self.request.GET.get('keyword','')
        })
        return context

    def get_queryset(self):
        queryset=super().get_queryset()
        keyword=self.request.GET.get('keyword','')
        if not keyword:
            return queryset

        return queryset.filter(Q(title__icontains=keyword) | Q(desc__icontains=keyword))


# 作者页面
class AuthorView(IndexView):
    def get_queryset(self):
        queryset=super().get_queryset()
        author_id=self.kwargs.get('owner_id')
        return queryset.filter(owner_id=author_id)