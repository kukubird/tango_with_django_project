from django.contrib import admin
from rango.models import Category, Page
from rango.models import UserProfile # can also be added to the above import so at its Category, Page, UserProfile as one import statement


admin.site.register(Category)
#admin.site.register(Page)


class PageAdmin(admin.ModelAdmin):
    list_display = ('category', 'title', 'url')
admin.site.register(Page, PageAdmin)
admin.site.register(UserProfile)
