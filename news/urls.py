from django.urls import path
from news.views import news, news_detail, news_comment, news_category, news_search

app_name = 'news'
urlpatterns = [
    path('', news, name='news_list'),
    path('<int:news_id>/',  news_detail, name='news_detail'),
    path('comment/<int:news_id>/', news_comment, name='news_comment'),
    path('category/<int:category_id>/', news_category, name='news_category'),
    path('search/', news_search, name='news_search'),
]
