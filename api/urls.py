from django.urls import path

from . import views

urlpatterns = [
    path('version', views.version, name='Version'),
    path('balcony', views.balcony, name='Balcony'),
    path('kpi', views.kpi, name='KPI'),
]
