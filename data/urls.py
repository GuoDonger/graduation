from django.urls import path
from data.views import data_list, data_detail, data_search, data_order


app_name = 'data'
urlpatterns = [
    path('', data_list, name='data_list'),
    path('<int:city_id>', data_detail, name='data_detail'),
    path('data_search/', data_search, name='data_search'),
    path('data_order/', data_order, name='data_order'),
]