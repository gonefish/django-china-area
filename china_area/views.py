# Create your views here.


from django.http import HttpResponse

import json

from china_area.models import Area, City, Province


def province_json(request):
    data = []

    for obj in Province.objects.all():
        data.append({'provinceID': obj.provinceID, 'province': obj.province})

    data_json = json.dumps(data, ensure_ascii=False)

    return HttpResponse(data_json, content_type='application/json; charset=utf-8')

def city_json(request, provinceID):
    data = []

    for obj in City.objects.filter(father__exact=provinceID):
        data.append({'cityID': obj.cityID, 'city': obj.city})

    data_json = json.dumps(data, ensure_ascii=False)

    return HttpResponse(data_json, content_type='application/json; charset=utf-8')

def area_json(request, cityID):
    data = []

    for obj in City.objects.filter(father__exact=cityID):
        data.append({'areaID': obj.areaID, 'area': obj.area})

    data_json = json.dumps(data, ensure_ascii=False)

    return HttpResponse(data_json, content_type='application/json; charset=utf-8')