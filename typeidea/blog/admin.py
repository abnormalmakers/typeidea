from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from .adminforms import PostAdminForm
from .models import Category,Tag,Post
from typeidea.custom_site import custom_site
from typeidea.base_admin import BaseOwnerAdmin
from django.contrib.admin.models import LogEntry
# Register your models here.

class PostInline(admin.TabularInline):
    fields=('title','desc')
    extra=1
    model=Post

class CategortOwnFilter(admin.SimpleListFilter):
    """ 自定义过滤器只显示当前用户分类 """

    title = '分类过滤器'
    parameter_name = 'owner_category'

    def lookups(self, request, model_admin):
        return Category.objects.filter(owner=request.user).values_list('id','name')

    def queryset(self,request,queryset):
        category_id=self.value()
        if category_id:
            return queryset.filter(category_id=self.value())
        return queryset


@admin.register(Category)
class CategoryAdmin(BaseOwnerAdmin):
    inlines=[PostInline,]
    list_display=('name','status','is_nav','owner','created_time')
    list_filter=['name']
    fields=('name','status','is_nav')

    def post_count(self,obj):
        print(obj)
        return obj.post_set.count()
    post_count.short_description='数量'



@admin.register(Tag)
class TagAdmin(BaseOwnerAdmin):
    list_display =('name','status','created_time')
    fields=('name','status')





@admin.register(Post,site=custom_site)
class PostAdmin(BaseOwnerAdmin):
    form=PostAdminForm
    list_filter = [CategortOwnFilter,]
    list_display = ('title','category','status','created_time','owner','operator')
    # list_filter = ['category']
    search_fields = ('title','category__name')

    actions_on_top = True
    actions_on_bottom = True
    save_on_top = True

    #指定哪些字段不展示
    exclude = ('owner',)

    # fields = (
    #     ('category','title'),
    #     'desc',
    #     'status',
    #     'content',
    #     'tag'
    # )

    fieldsets=(
        ('基础配置',{
            'description':'这里是基础配置，通过description控制',
            'fields':(
                ('title','category'),
                'status'
            )
        }),
        ('内容',{
            'description': '这里是内容',
            'fields':(
                'desc',
                'content'
            )
        }),
        ('额外信息',{
            'classes':('collapse',),
            'fields':('tag',)
        })
    )

    def operator(self,obj):
        return format_html(
            '<a href="{}">编辑</a>',
            reverse('cus_admin:blog_post_change',args=(obj.id,))
        )
    operator.short_description = '操作'


@admin.register(LogEntry,site=custom_site)
class LogEntryAdmin(admin.ModelAdmin):
    list_display = ['object_repr','object_id','action_flag','user','change_message']
