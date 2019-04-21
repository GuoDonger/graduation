from django.contrib import admin
from data.models import City, Data


# Register your models here.
class CityAdmin(admin.ModelAdmin):
    list_display = ['id', 'initial', 'city', 'word']


class DataAdmin(admin.ModelAdmin):
    list_display = ['city', 'time', 'AQI']


admin.site.register(City, CityAdmin)
admin.site.register(Data, DataAdmin)
