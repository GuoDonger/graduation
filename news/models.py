from django.db import models
from datetime import datetime
from user.models import UserProfile


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=10, verbose_name='类名')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '类别表'
        verbose_name_plural = verbose_name


class News(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='类别')
    title = models.CharField(max_length=100, null=False, verbose_name='标题')
    content = models.TextField(verbose_name='内容')
    author = models.CharField(max_length=50, verbose_name='作者')
    image = models.ImageField(upload_to='news/%y/%m/%d', max_length=100, verbose_name='新闻图片')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '新闻表'
        verbose_name_plural = verbose_name


class Comment(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE, verbose_name='新闻')
    name = models.CharField(max_length=50, default='匿名', verbose_name='姓名')
    email = models.CharField(max_length=50, verbose_name='邮箱')
    content = models.TextField(verbose_name='内容')
    time = models.DateTimeField(default=datetime.now, verbose_name='评论时间')

    class Meta:
        verbose_name = '评论表'
        verbose_name_plural = verbose_name
