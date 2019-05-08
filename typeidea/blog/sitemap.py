from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from .models import Post

class PostSitemap(Sitemap):
    changefreq='always'
    priority=1.0
    protocol='https'
    
    
    def items(self):
        return Post.objects.filter(status=Post.STATUS_NORMAL)
    
    def lastmod(self,object):
        return object.created_time
    
    def location(self,object):
        return reverse('post-detail',args=(object.pk,))