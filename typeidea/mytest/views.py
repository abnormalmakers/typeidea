from django.http import HttpResponse
from django.shortcuts import render
from .models import *
# Create your views here.
from django.views import View


class Mytest(View):
    def get(self,request):
        manya=ManyA.objects.filter(id=1)
        manyb=manya.filter(manyb__id=1)
        print(manyb)
        for i in manyb:
            print(i.name)
        return HttpResponse('ok')