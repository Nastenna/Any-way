from django.urls import path

from . import views

urlpatterns = [
    path('routes/', views.routes, name='routes'),
    path('', views.new_route_params, name='index'),
    path('points/', views.PointsView.as_view(), name='points'),
    path('point/<int:pk>/', views.PointView.as_view(), name='point'),
    path('route/<int:pk>/', views.RouteView.as_view(), name='route'),
    # path('login/', views.login, name='login'),
    path('register/', views.register, name='register')
]