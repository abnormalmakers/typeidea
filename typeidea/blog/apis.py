from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

from blog.models import Post, Category, Tag
from blog.serializer import PostSerializer, PostDetailSerializer, CategorySerializer, TagSerializer


#最新文章列表api
class PostViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = PostSerializer
    queryset=Post.objects.filter(status=Post.STATUS_NORMAL)
    permission_classes = [IsAdminUser]

    def retrieve(self, request, *args, **kwargs):
        self.serializer_class=PostDetailSerializer
        return super().retrieve(request,*args,**kwargs)

    # 通过分类获取文章列表api
    def filter_queryset(self, queryset):
        category_id=self.request.query_params.get('category')
        tag_id=self.request.query_params.get('tag')
        print(tag_id)
        if category_id:
            queryset=Post.objects.filter(category_id=category_id)
        elif tag_id:
            queryset=Post.objects.filter(tag__id=tag_id)
        return queryset

#分类列表api
class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset=Category.objects.filter(status=Category.STATUS_NORMAL)
    permission_classes = [IsAdminUser]


#标签列表api
class TagViewSet(viewsets.ModelViewSet):
    serializer_class = TagSerializer
    queryset=Tag.objects.filter(status=Tag.STATUS_NORMAL)
    permission_classes = [IsAdminUser]


