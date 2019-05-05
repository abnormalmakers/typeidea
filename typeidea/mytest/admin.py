from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(ManyA)
class ManyAadmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(ManyB)
class ManyBadmin(admin.ModelAdmin):
    list_display = ('name',)