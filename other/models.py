from django.db import models
from datetime import datetime


# Create your models here.
class Banner(models.Model):
    title = models.CharField(max_length=100, verbose_name='轮播标题', null=False)
    content = models.TextField(verbose_name='内容', null=False)
    image = models.ImageField(upload_to='banner/%y/%m', max_length=100, verbose_name='轮播图片')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '轮播内容'
        verbose_name_plural = verbose_name

