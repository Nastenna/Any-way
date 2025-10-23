from django.contrib import admin

from . models import Point
# Register your models here.


class POIAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,          {'fields': ['name', 'description', 'time_for_viewing', 'image', 'is_entry_point']}),
        ('Координаты',  {'fields': ['x_coord', 'y_coord']})
    ]
    list_display = ('name', 'time_for_viewing', 'is_entry_point')


admin.site.register(Point, POIAdmin)
