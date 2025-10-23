from django import forms
from .models import Point


class NewRouteForm(forms.Form):
    route_length = forms.CharField(label="Желаемое время (минуты)")
    required_point = forms.ModelChoiceField(label="Точка для посещения (опционально)",
                                            queryset=Point.objects.all())

