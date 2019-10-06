from django.urls import path
from . import views
from dokumenty.views import CrashReport
from podstrony.views import (start, raporty, nowyraport, protokoly, faktury)

urlpatterns = [
    path('', views.start, name='home'),
    path('raporty', raporty),
    path('nowyraport', nowyraport),
    path('protokoly', protokoly),
    path('opis', CrashReport),
    path('faktury', faktury),


]