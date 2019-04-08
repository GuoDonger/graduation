from django.contrib import admin
from other.models import Banner


# Register your models here.
class BannerAdmin(admin.ModelAdmin):
    list_display = ['title', ]


admin.site.register(Banner, BannerAdmin)
