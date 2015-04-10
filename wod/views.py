from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

from .models import Wod

def wod_index(request):
    latest_wod_list = Wod.objects.order_by('-date')[:5]
    context = RequestContext(request, {
        'latest_wod_list': latest_wod_list,
    })

    return render(request, "wod/index.html", context)

def wod_details(request, wod_id):
    response = "You're looking at the results of wod # %s."
    return HttpResponse(response % wod_id)
