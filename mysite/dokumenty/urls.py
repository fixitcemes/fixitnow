from django.urls import path, reverse

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('crashreports/', views.CrashReportsListView.as_view(), name='crashreports'),
    path('crashreport/<int:pk>', views.CrashReportsDetailView.as_view(), name='crashreport-detail'),

]