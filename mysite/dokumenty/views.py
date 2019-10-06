from django.shortcuts import render
from .models import CrashReport


# Create your views here.

def CrashReport(request):
    obj = report.objects.get(id=1)
    context = {
        'object': obj

    }
    return render(request, "form/opis.html", context)
