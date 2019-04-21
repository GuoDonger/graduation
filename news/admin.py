from django.contrib import admin
from news.models import News, Category, Comment


# Register your models here.
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'source']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', ]


class CommentAdmin(admin.ModelAdmin):
    list_display = ['news', 'user', 'content']


admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)
