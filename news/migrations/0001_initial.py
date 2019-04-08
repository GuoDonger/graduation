# Generated by Django 2.0.6 on 2019-03-16 16:30

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, verbose_name='类名')),
            ],
            options={
                'verbose_name': '类别表',
                'verbose_name_plural': '类别表',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=50, verbose_name='邮箱')),
                ('content', models.TextField(verbose_name='内容')),
                ('time', models.DateTimeField(default=datetime.datetime.now, verbose_name='评论时间')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name': '评论表',
                'verbose_name_plural': '评论表',
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='标题')),
                ('content', models.TextField(verbose_name='内容')),
                ('author', models.CharField(max_length=50, verbose_name='作者')),
                ('image', models.ImageField(upload_to='news/%y/%m/%d', verbose_name='新闻图片')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.Category', verbose_name='类别')),
            ],
            options={
                'verbose_name': '新闻表',
                'verbose_name_plural': '新闻表',
            },
        ),
        migrations.AddField(
            model_name='comment',
            name='news',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.News', verbose_name='新闻'),
        ),
    ]