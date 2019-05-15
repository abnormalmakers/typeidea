from rest_framework import serializers

from .models import Post, Category


class PostSerializer(serializers.ModelSerializer):
    category=serializers.SlugRelatedField(
        read_only=True,  #定义外键数据是否可写
        slug_field='name'   #指定显示的字段
    )

    tag=serializers.SlugRelatedField(
        many=True,   #多对多
        read_only=True,
        slug_field='name'
    )

    owner=serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )
    created_time=serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')

    url=serializers.HyperlinkedIdentityField(view_name='api-post-detail')

    class Meta:
        model = Post
        fields = ['url', 'id', 'title', 'category', 'tag', 'owner', 'created_time']
        # extra_kwargs = {
        #     'url': {'view_name': 'api-post-detail'}
        # }



class PostDetailSerializer(PostSerializer):
    class Meta:
        model=Post
        fields=['id','title','category','tag','owner','owner','content_html','created_time']


class CategorySerializer(serializers.ModelSerializer):
    created_time=serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')
    class Meta:
        model=Category
        fields=['id','name','created_time']


