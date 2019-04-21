# Generated by Django 2.1.7 on 2019-04-20 13:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('initial', models.CharField(max_length=10, verbose_name='首字母')),
                ('city', models.CharField(max_length=30, verbose_name='城市')),
                ('word', models.CharField(max_length=30, verbose_name='拼音')),
            ],
            options={
                'verbose_name': '城市',
                'verbose_name_plural': '城市',
            },
        ),
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(verbose_name='时间')),
                ('data', models.TextField(verbose_name='数据')),
                ('AQI', models.IntegerField(verbose_name='AQI')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.City', verbose_name='所属城市')),
            ],
            options={
                'verbose_name': '数据',
                'verbose_name_plural': '数据',
            },
        ),
    ]
