from django.db import models


# Create your models here.
class City(models.Model):
    initial = models.CharField(max_length=10, verbose_name='首字母')
    city = models.CharField(max_length=30, verbose_name='城市')
    word = models.CharField(max_length=30, verbose_name='拼音')

    def __str__(self):
        return self.city

    class Meta:
        verbose_name = '城市'
        verbose_name_plural = verbose_name


class Data(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name='所属城市')
    time = models.DateTimeField(verbose_name='时间')
    data = models.TextField(verbose_name='数据')
    AQI = models.IntegerField(verbose_name='AQI')

    class Meta:
        verbose_name = '数据'
        verbose_name_plural = verbose_name
