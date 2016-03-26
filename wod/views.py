from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.template import RequestContext, loader, Context
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from django.views.generic import FormView, RedirectView
from django.contrib.auth.forms import AuthenticationForm

from .models import Wod
from core.forms import UserForm

@login_required(login_url = 'login')
def wod_index(request):
    latest_wod_list = Wod.objects.order_by('-date')[:5]
    context = RequestContext(request, {
        'latest_wod_list': latest_wod_list,
    })

    return render(request, "wod/wod_archive.html", context)

@login_required(login_url = 'login')
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

class RegisterView(FormView):

    template_name = 'wod/register.html'
    form_class = UserForm
    success_url = '/login/'

    def dispatch(self, *args, **kwargs):
        return super(RegisterView, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        new_user = User.objects.create_user(**form.cleaned_data)
        new_user.save()
        return super(RegisterView, self).form_valid(form)

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

class LogoutView(RedirectView):

    template_name = 'wod/logout.html'
    url = '/home/'

    def get(self, request, *args, **kwargs):
        logout(self.request)
        return super(LogoutView, self).get(request, *args, **kwargs)
