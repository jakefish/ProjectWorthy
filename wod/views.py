from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import login
from django.template import RequestContext, loader, Context
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import FormView
from core.forms import UserForm

from .models import Wod


def wod_index(request):
    latest_wod_list = Wod.objects.order_by('-date')[:5]
    context = RequestContext(request, {
        'latest_wod_list': latest_wod_list,
    })

    return render(request, "wod/wod_archive.html", context)

def wod_details(request, wod_id):
    wod = Wod.objects.get(id=wod_id)
    return render(request, "wod/wod_page.html", {"wod": wod} )

class LoginView(FormView):
    template_name = 'wod/login.html'
    form_class = UserForm
    success_url = '/home/'


    def dispatch(self, *args, **kwargs):
        return super(LoginView, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(LoginView, self).form_valid(form)
    
