from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from data.tasks import get_order
from data.models import City, Data


# Create your views here.
def data_list(request):
    cities = City.objects.all()
    return render(request, 'data_list.html', {'cities': cities})


def data_detail(request, city_id):
    datas = Data.objects.all().filter(city_id=city_id)[0]
    get_order.delay()
    if datas:
        first_ten = Data.objects.all().order_by('AQI')[:10]
        end_ten = Data.objects.all().order_by('-AQI')[:10]
        area1 = []
        AQI1 = []
        for data in first_ten:
            area1.append(data.city.city)
            AQI1.append(data.AQI)
        area2 = []
        AQI2 = []
        for data in end_ten:
            area2.append(data.city.city)
            AQI2.append(data.AQI)
        return render(request, 'data_detail.html',
                      {'datas': datas, 'area1': area1, 'AQI1': AQI1, 'area2': area2, 'AQI2': AQI2})
    else:
        return HttpResponse('暂无该城市的数据')


def data_order(request):
    datas = Data.objects.all().order_by('AQI')
    ranks = {}
    for data in datas:
        if 0 < data.AQI <= 50:
            ranks[data] = '优质'
        elif 50 < data.AQI <= 100:
            ranks[data] = '良好'
        elif 100 < data.AQI <= 150:
            ranks[data] = '轻度污染'
        elif 150 < data.AQI <= 200:
            ranks[data] = '中度污染'
        elif 200 < data.AQI <= 300:
            ranks[ data] ='重度污染'
        else:
            ranks[data] = '严重污染'
    return render(request, 'data_order.html', {'datas': datas, 'ranks': ranks})


def data_search(request):
    search = request.POST.get('search')
    city = City.objects.all().filter(city=search)[0]
    if city:
        city_id = city.id
        data = Data.objects.all().filter(city_id=city_id)[0]
        if data:
            return redirect(reverse('data:data_detail', kwargs={'city_id': city_id}))
        else:
            HttpResponse('暂时无该城市的数据<a href="http://127.0.0.1:8000/data/">返回</a>')
    else:
        return HttpResponse('没有该城市<a href="http://127.0.0.1:8000/data/">返回</a>')
