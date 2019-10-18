from django.shortcuts import render
from django.views import generic
from .models import CrashReport, ServiceReport


def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_crashreports = CrashReport.objects.all().count()
    # num_instances = BookInstance.objects.all().count()

    # Opens Crashreports (status = 'o')
    #  num_crashreport_open = CrashReport.objects.filter(status__exact='o').count()

    context = {
        'num_crashreports': num_crashreports,
        #   'num_crashreports_processing': num_crashreports_processing,
        #   'num_crashreports_open': num_crashreports_open,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'dokumenty/index.html', context=context)


class CrashReportsListView(generic.ListView):
    model = CrashReport
    context_object_name = 'crash_reports_list'  # your own name for the list as a template variable
    queryset = CrashReport.objects.filter()[:5]  # Get 5 crash reports


class CrashReportsDetailView(generic.DetailView):
    model = CrashReport


class ServiceReportsListView(generic.ListView):
    model = ServiceReport
    context_object_name = 'service_reports_list'  # your own name for the list as a template variable
    queryset = ServiceReport.objects.filter()[:5]  # Get 5 crash reports


class ServiceReportsDetailView(generic.DetailView):
    model = ServiceReport


def nowyraport(request, *args, **kwargs):
    return render(request, "dokumenty/nowyraport.html", {})


def protokoly(request, *args, **kwargs):
    return render(request, "dokumenty/protokoly.html", {})


def faktury(request, *args, **kwargs):
    return render(request, "dokumenty/faktury.html", {})
