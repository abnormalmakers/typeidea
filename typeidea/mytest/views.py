from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView

from .models import *
# Create your views here.
from django.views import View


# class Mytest(View):
#     def get(self,request):
#         manya=ManyA.objects.filter(id=1)
#         manyb=manya.filter(manyb__id=1)
#         print(manyb)
#         for i in manyb:
#             print(i.name)
#         return HttpResponse('ok')

class MytestA(ListView):
    model=ManyA
    template_name = 'mytest/manya.html'


class MytestB(ListView):
    model=ManyB
    template_name = 'mytest/manyb.html'