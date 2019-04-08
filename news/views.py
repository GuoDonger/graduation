from django.http import HttpResponse
from django.shortcuts import render
from news.models import News, Comment
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q


# Create your views here.
def news(request):
    news_list = News.objects.all().order_by('add_time')
    page_num = request.GET.get('page', 1)
    paginator = Paginator(news_list, 5)
    try:
        page_list = paginator.page(page_num)
    except PageNotAnInteger:
        page_list = paginator.page(1)
    except EmptyPage:
        page_list = paginator.page(paginator.num_pages)
    return render(request, 'news_list.html', {'news_list': news_list, 'page_list': page_list})


def news_detail(request, news_id):
    single_news = News.objects.filter(pk=news_id)[0]
    comments = Comment.objects.filter(Q(news=news_id)).all()
    other_news = News.objects.filter(Q(category=single_news.category))[:5]
    page_num = request.GET.get('page', 1)
    paginator = Paginator(comments, 3)
    try:
        page_list = paginator.page(page_num)
    except PageNotAnInteger:
        page_list = paginator.page(1)
    except EmptyPage:
        page_list = paginator.page(paginator.num_pages)
    return render(request, 'news_detail.html',
                  {'news': single_news, 'comments': comments, 'other_news': other_news, 'page_list': page_list})


def news_comment(request, news_id):
    comment_news = News.objects.filter(pk=news_id)[0]
    name = request.POST.get('name')
    email = request.POST.get('email')
    content = request.POST.get('comment')
    comment = Comment()
    comment.news = comment_news
    comment.name = name
    comment.email = email
    comment.content = content
    comment.save()
    return HttpResponse('评论成功<a href="http://127.0.0.1:8000">返回首页</a>')
