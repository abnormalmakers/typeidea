from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from blog.views import CommonViewMixin
from config.models import Link


class LinkListView(CommonViewMixin,ListView):
    model=Link
    context_object_name = 'links'
    template_name = 'config/links.html'

    def get_queryset(self):
        queryset=Link.objects.filter(status=Link.STATUS_NORMAL)
        return queryset