from django.contrib import admin
from news.models import News, Category


# Register your models here.
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'author']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', ]


admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)
