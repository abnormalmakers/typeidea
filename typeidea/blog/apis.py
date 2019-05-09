from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Post
from .serializer import PostSeializer

@api_view()
def post_list(request):
    posts=Post.objects.filter(status=Post.STATUS_NORMAL)
    post_serializers=PostSeializer(posts,many=True)
    return Response(post_serializers.data)


class PostList(generics.ListCreateAPIView):
    queryset=Post.objects.filter(status=Post.STATUS_NORMAL)
    serializer_class = PostSeializer