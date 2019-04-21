# Generated by Django 2.1.7 on 2019-04-20 15:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_comment_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='内容')),
            ],
            options={
                'verbose_name': '内容表',
                'verbose_name_plural': '内容表',
            },
        ),
        migrations.RemoveField(
            model_name='news',
            name='content',
        ),
        migrations.AddField(
            model_name='content',
            name='news',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.News', verbose_name='所属新闻'),
        ),
    ]
