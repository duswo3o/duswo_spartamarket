from django.shortcuts import render, redirect

from django.views.decorators.http import require_http_methods, require_POST
# from django.contrib.auth import
# Create your views here.


def index(request):
    return render(request, "products/index.html")