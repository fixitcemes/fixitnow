from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('crashreports/', views.CrashReportsListView.as_view(), name='crashreports'),
]