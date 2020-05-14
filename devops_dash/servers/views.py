from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return HttpResponse("Bismillah. You're at the polls index.")