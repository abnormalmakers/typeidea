from django.contrib import admin

class BaseOwnerAdmin(admin.ModelAdmin):
    exclude=('owner',)

    # get_queryset只显示当前登录用户自己的内容
    def get_queryset(self, request):
        qs=super(BaseOwnerAdmin,self).get_queryset(request)
        return qs.filter(owner=request.user)

    # save_model禁止作者篡改分类作者
    def save_model(self, request, obj, form, change):
        obj.owner=request.user
        return super(BaseOwnerAdmin,self).save_model(request, obj, form, change)