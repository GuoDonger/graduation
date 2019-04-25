from django.urls import path
from other.views import index, harm, governance, about


app_name = 'other'
urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('harm/', harm, name='harm'),
    path('governance/', governance, name='governance'),
]