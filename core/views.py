from django.shortcuts import render
from django.views.generic import TemplateView

class CoreView(TemplateView):

    template_name = 'site_base.html'
    
