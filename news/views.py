from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import render, redirect
from news.models import News, Comment, Category, Content
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


# Create your views here.
def news(request):
    news_list = News.objects.all().order_by('-add_time')
    paginator = Paginator(news_list, 10)
    categories = Category.objects.all()
    try:
        current_page_num = int(request.GET.get('page'))
        current_page = paginator.page(current_page_num)
        if paginator.num_pages > 11:
            if current_page_num - 5 < 1:
                page_range = range(1, 12)
            elif current_page_num + 5 > paginator.num_pages:
                page_range = range(paginator.num_pages - 10, paginator.num_pages + 1)
            else:
                page_range = range(current_page_num - 5, current_page_num + 6)
        else:
            page_range = paginator.page_range
    except Exception as error:
        current_page_num = 1
        current_page = paginator.page(current_page_num)
    return render(request, 'news_list.html', locals())


def news_category(request, category_id):
    category = Category.objects.filter(id=category_id)[0]
    news_list = News.objects.all().filter(category_id=category_id)
    categories = Category.objects.all()
    page_num = request.GET.get('page', 1)
    paginator = Paginator(news_list, 10)
    try:
        page_list = paginator.page(page_num)
    except PageNotAnInteger:
        page_list = paginator.page(1)
    except EmptyPage:
        page_list = paginator.page(paginator.num_pages)
    return render(request, 'news_category.html',
                  {'news_list': news_list, 'page_list': page_list, 'category': category, 'categories': categories})


def news_search(request):
    search = request.POST.get('search')
    news_list = News.objects.all().filter(title__contains=search)
    categories = Category.objects.all()
    if news_list:
        page_num = request.GET.get('page', 1)
        paginator = Paginator(news_list, 10)
        try:
            page_list = paginator.page(page_num)
        except PageNotAnInteger:
            page_list = paginator.page(1)
        except EmptyPage:
            page_list = paginator.page(paginator.num_pages)
        return render(request, 'news_search.html',
                      {'news_list': news_list, 'page_list': page_list, 'categories': categories})
    else:
        return HttpResponse('无相关新闻 <a href="http://127.0.0.1:8000/news/">返回</a>')


def news_detail(request, news_id):
    single_news = News.objects.filter(pk=news_id)[0]
    content = Content.objects.all().filter(news_id=news_id)
    other_news = News.objects.filter(category=single_news.category)[:5]
    comments = Comment.objects.filter(news=news_id).all()
    page_num = request.GET.get('page', 1)
    paginator = Paginator(comments, 5)
    try:
        page_list = paginator.page(page_num)
    except PageNotAnInteger:
        page_list = paginator.page(1)
    except EmptyPage:
        page_list = paginator.page(paginator.num_pages)
    return render(request, 'news_detail.html',
                  {'news': single_news, 'content': content, 'comments': comments, 'other_news': other_news,
                   'page_list': page_list})


def news_comment(request, news_id):
    comment_news = News.objects.filter(pk=news_id)[0]
    user = request.user
    content = request.POST.get('comment')
    comment = Comment()
    comment.news = comment_news
    comment.user = user
    comment.content = content
    comment.save()
    return redirect(reverse('news:news_detail', kwargs={'news_id': news_id}))
