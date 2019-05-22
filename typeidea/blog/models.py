import mistune
from django.core.cache import cache
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.utils.functional import cached_property


class Category(models.Model):
    STATUS_NORMAL=1
    STATUS_DELETE=0
    STATUS_ITEMS=(
        (STATUS_NORMAL,'正常'),
        (STATUS_DELETE,'删除'),
    )

    name=models.CharField(max_length=50,verbose_name='名称')
    status=models.PositiveIntegerField(default=STATUS_NORMAL,choices=STATUS_ITEMS,verbose_name='状态')
    is_nav=models.BooleanField(verbose_name='是否为导航',default=False)
    created_time=models.DateTimeField(auto_now_add=True,verbose_name='创建时间')
    owner=models.ForeignKey(User,verbose_name='作者')

    @classmethod
    def get_navs(cls):
        categorys=Category.objects.filter(status=cls.STATUS_NORMAL)
        nav_category=[]
        normal_category=[]
        for category in categorys:
            if category.is_nav:
                nav_category.append(category)
            else:
                normal_category.append(category)

        return {
            'navs':nav_category,
            'categories':normal_category
        }


    def __str__(self):
        return self.name

    class Meta:
        db_table='category'
        verbose_name=verbose_name_plural='分类'



class Tag(models.Model):
    STATUS_NORMAL=1
    STATUS_DELETE=0
    STATUS_ITEM=(
        (STATUS_NORMAL,'正常'),
        (STATUS_DELETE,'删除')
    )
    name=models.CharField(max_length=10,verbose_name='名称')
    status=models.PositiveIntegerField(default=STATUS_NORMAL,choices=STATUS_ITEM,verbose_name='名称')
    created_time=models.DateTimeField(auto_now_add=True,verbose_name='创建时间')
    owner=models.ForeignKey(User,verbose_name='作者')

    @classmethod
    def get_tag_all(cls):
        return cls.objects.filter(status=cls.STATUS_NORMAL)

    def __str__(self):
        return self.name

    class Meta:
        db_table='tag'
        verbose_name=verbose_name_plural='标签'


class Post(models.Model):
    STATUS_NORMAL=1
    STATUS_DELETE=0
    STATUS_ITEM=(
        (STATUS_NORMAL,'正常'),
        (STATUS_DELETE,'删除')
    )

    title=models.CharField(max_length=255,verbose_name='标题')
    desc=models.CharField(max_length=1024,blank=True,verbose_name='摘要')
    content=models.TextField(verbose_name='正文',help_text='正文必须为MarkDown格式')
    content_html=models.TextField(verbose_name='正文html代码',blank=True,editable=False)
    status=models.PositiveIntegerField(default=STATUS_NORMAL,choices=STATUS_ITEM,verbose_name='状态')
    created_time=models.DateTimeField(auto_now_add=True,verbose_name='创建时间')
    category=models.ForeignKey(Category,verbose_name='分类')
    tag=models.ManyToManyField(Tag,verbose_name='标签')
    owner=models.ForeignKey(User,verbose_name='作者')
    pv=models.PositiveIntegerField(default=1)
    uv=models.PositiveIntegerField(default=1)

    @classmethod
    def latest_posts(cls):
        query_set=cache.get('latest_posts')
        if not query_set:
            query_set=cls.objects.filter(status=cls.STATUS_NORMAL)[:5]
            cache.set('latest_posts',query_set,60)
        return query_set

    @classmethod
    def hot_posts(cls):
        result = cache.get('hot_posts')
        if not result:
            result=cls.objects.filter(status=cls.STATUS_NORMAL).order_by('-pv')[:5]
            cache.set('host_posts',result,10*60)
        return result

    def __str__(self):
        return self.title

    def save(self,*args,**kwargs):
        self.content_html=mistune.markdown(self.content)
        super().save(*args,**kwargs)

    @cached_property
    def tags(self):
        return ','.join(self.tag.values_list('name',flat=True))

    class Meta:
        db_table='post'
        verbose_name=verbose_name_plural='文章'
        ordering=['-id']

    @staticmethod
    def get_by_tag(tag_id):
        post_list=[]
        try:
            tag=Tag.objects.get(id=tag_id)
        except Tag.DoseNotExist:
            tag=None
        else:
            post_list=tag.post_set.filter(status=Post.STATUS_NORMAL).select_related('owner','category')
        return post_list,tag


    @staticmethod
    def get_by_category(category_id):
        post_list = []
        try:
            category=Category.objects.get(category_id)
        except Category.DoseNotExist:
            category=None
        else:
            post_list=category.post_set.all().select_related('owner','category')

        return post_list,category


