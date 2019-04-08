from django.urls import path
from data.views import data


app_name = 'data'
urlpatterns = [
    path('', data, name='data_show'),

]