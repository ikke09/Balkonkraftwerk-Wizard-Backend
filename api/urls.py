from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('version', views.Version.as_view(), name='Version'),
    path('balcony', views.Balcony.as_view(), name='Balcony'),
    path('kpi', views.KPI.as_view(), name='KPI'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
