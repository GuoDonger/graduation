# Generated by Django 2.1.7 on 2019-04-23 15:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='轮播标题')),
                ('content', models.TextField(verbose_name='内容')),
                ('image', models.ImageField(upload_to='banner/%y/%m', verbose_name='轮播图片')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '轮播内容',
                'verbose_name_plural': '轮播内容',
            },
        ),
    ]
