from rest_framework import serializers

from .models import Post

class PostSeializer(serializers.ModelSerializer):
    class Meta:
        model=Post
        fields=['title','category','desc','content_html','created_time']
