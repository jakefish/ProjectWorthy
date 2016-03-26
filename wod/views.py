from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.template import RequestContext, loader, Context
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from django.views.generic.edit import FormView
from core.forms import UserForm
from django.contrib.auth.forms import AuthenticationForm

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
    form_class = AuthenticationForm
    success_url = '/home/'


    def dispatch(self, *args, **kwargs):
        return super(LoginView, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        username = self.request.POST['username']
        password = self.request.POST['password']
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return super(LoginView, self).form_valid(form)

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
