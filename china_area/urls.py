from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^province/$', 'china_area.views.province_json'),
    url(r'^city/(?P<provinceID>\d{6})/$', 'china_area.views.city_json'),
    url(r'^area/(?P<cityID>\d{6})/$', 'china_area.views.area_json')
)
