from django.urls import path
from news.views import news, news_detail, news_comment

app_name = 'news'
urlpatterns = [
    path('', news, name='news_list'),
    path('<int:news_id>/',  news_detail, name='news_detail'),
    path('comment/<int:news_id>/', news_comment, name='comment'),
]
