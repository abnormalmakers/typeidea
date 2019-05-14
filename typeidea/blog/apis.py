from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

from blog.models import Post, Category
from blog.serializer import PostSerializer, PostDetailSerializer,CategorySerializer


class PostViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = PostSerializer
    queryset=Post.objects.filter(status=Post.STATUS_NORMAL)
    permission_classes = [IsAdminUser]

    def retrieve(self, request, *args, **kwargs):
        self.serializer_class=PostDetailSerializer
        return super().retrieve(request,*args,**kwargs)




class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset=Category.objects.filter(status=Category.STATUS_NORMAL)
    permission_classes = [IsAdminUser]
