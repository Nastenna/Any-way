import math

from django.db import models

from .logic.graph import *

# Create your models here.


class Point(models.Model):
    name = models.CharField('Название', max_length=200)
    description = models.TextField('Описание', max_length=2000)
    x_coord = models.FloatField('Широта')
    y_coord = models.FloatField('Долгота')
    time_for_viewing = models.IntegerField('Время на осмотр', default=5)
    image = models.ImageField('Изображение', null=True, blank=True)
    is_entry_point = models.BooleanField("Начальная точка", default=False)

    def __str__(self):
        return self.name

    def distance(self, other: 'Point') -> float:
        """Get distance in meters."""
        return haversine(self.x_coord, self.y_coord, other.x_coord, other.y_coord) * 1000


class Route(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField('Дата создания')
    visited = models.DateTimeField('Дата прохождения', null=True)
    user_id = models.IntegerField(null=True)  # Public route if user_is is null
    is_static = models.BooleanField(default=True)
    description = models.TextField(max_length=2000)

    def __str__(self):
        return self.name

    def make_static(self):
        self.is_static = True
        self.save()


class RouteNode(models.Model):
    point = models.ForeignKey(Point, on_delete=models.RESTRICT)
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    distance_to_prev = models.FloatField()
    number_in_route = models.IntegerField()
