from django.db import models


class Area(models.Model):

    areaID = models.CharField('areaID', max_length=6, unique=True)
    area = models.CharField('area', max_length=60)
    father = models.CharField('father', max_length=6)

    def __unicode__(self):
        return self.area

class City(models.Model):
    cityID = models.CharField('cityID', max_length=6, unique=True)
    city = models.CharField('city', max_length=60,)
    father = models.CharField('father', max_length=6)

    def __unicode__(self):
            return self.city
                    

class Province(models.Model):

    provinceID = models.CharField('provinceID', max_length=6, unique=True)
    province = models.CharField('province', max_length=60)

    def __unicode__(self):
        return self.province
    