from django.db import models
from datetime import datetime
from user.models import UserProfile


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=30, verbose_name='类名')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '类别表'
        verbose_name_plural = verbose_name


class News(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='类别')
    title = models.CharField(max_length=100, verbose_name='标题')
    image = models.URLField(verbose_name='图片链接')
    source = models.CharField(max_length=50, verbose_name='来源')
    digest = models.TextField(verbose_name='摘要', default='')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='时间')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '新闻表'
        verbose_name_plural = verbose_name


class Content(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE, verbose_name='所属新闻')
    content = models.TextField(verbose_name='内容')

    class Meta:
        verbose_name = '内容表'
        verbose_name_plural = verbose_name


class Comment(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE, verbose_name='新闻')
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name='用户')
    content = models.TextField(verbose_name='内容')
    time = models.DateTimeField(default=datetime.now, verbose_name='评论时间')

    class Meta:
        verbose_name = '评论表'
        verbose_name_plural = verbose_name
