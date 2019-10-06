from django.http import HttpResponse
from django.shortcuts import render

def start(request, *args, **kwargs):
	return render(request, "podstrony/home.html", {})

def raporty(request, *args, **kwargs):
	return render(request, "podstrony/raporty.html", {})

def nowyraport (request, *args, **kwargs):
	return render(request, "podstrony/nowyraport.html", {})

def protokoly(request, *args, **kwargs):
	return render(request, "podstrony/protokoly.html", {})

def faktury(request, *args, **kwargs):
	return render(request, "podstrony/faktury.html", {})

