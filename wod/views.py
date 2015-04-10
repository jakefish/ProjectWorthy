from django.shortcuts import render
from django.http import HttpResponse

def wod_index(request):
    return HttpResponse("Hello, world. You're at the Wod index.")

def wod_details(request, wod_id):
    response = "You're looking at the results of wod # %s."
    return HttpResponse(response % wod_id)
