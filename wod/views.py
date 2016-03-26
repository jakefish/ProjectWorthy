from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_protect
from django.views.generic import FormView, RedirectView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.template import RequestContext, loader, Context

from .models import Wod
from core.forms import UserForm


@login_required(login_url = 'login')
def wod_index(request):
    """A view that displays the 5 most recently created Wods.

    Must be loggined in to access this view.

    Args:
        request:  Represents server-client relationship.

    Returns:
        A rendering of context, which contains the 5 most recently created
        Wods.
    """

    latest_wod_list = Wod.objects.order_by('-date')[:5]
    context = RequestContext(request, {
        'latest_wod_list': latest_wod_list,
    })

    return render(request, "wod/wod_archive.html", context)


@login_required(login_url = 'login')
def wod_details(request, wod_id):
    """A view that displays info for a specific wod.

    Displays info for a specific wod based on their unique wod_id.

    Args:
        request:  Represents server-client relationship.
        wod_id:   A wod objects unique id which is used to fetch the
                  request wod.

    """

    wod = Wod.objects.get(id=wod_id)

    return render(request, "wod/wod_page.html", {"wod": wod} )


class LoginView(FormView):
    """View to process user login.

    Inherits from django's form view class and overrides django's dispatch,
    form_valid, and post methods.

    Attributes:
        template_name:        A field that points to the template this view will
                              render to.

        form_class:           Stores the form that this class will revolve
                              around.

        success_url:          If the form is valid and submitted properly this
                              stores the url that is located after.
    """

    template_name = 'wod/login.html'
    form_class = AuthenticationForm
    success_url = '/home/'

    def dispatch(self, *args, **kwargs):
        """Overrides django's dispatch method.

        Args:
            self:              References the class itself.

            *args:             Stores uncertain amount of addition arguments
                               passed.

            **kwargs:          Allows the passing through keyword arguments to
                               provide a variable name as it is passed into
                               this function.
        """

        return super(LoginView, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        """Overrides django's form_valid method.

        Authenticates users based of their inputted credentials and logs them
        into the site if they are properly authenticated.

        Args:
            self:              References the class itself.

            form:              A reference to the form being processed, in this
                               case AuthenticationForm.

        """

        username = self.request.POST['username']
        password = self.request.POST['password']
        user = authenticate(username=username, password=password)
        login(self.request, user)

        return super(LoginView, self).form_valid(form)

    def post(self, request, *args, **kwargs):
        """Overrides django's post method.

        Args:
            self:              References the class itself.

            *args:             Stores uncertain amount of addition arguments
                               passed.

            **kwargs:          Allows the passing through keyword arguments to
                               provide a variable name as it is passed into
                               this function.
        """

        form_class = self.get_form_class()
        form = self.get_form(form_class)

        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class RegisterView(FormView):
    """View to process user registration.

    Inherits from django's form view class and overrides django's dispatch,
    form_valid, and post methods.

    Attributes:
        template_name:        A field that points to the template this view will
                              render to.

        form_class:           Stores the form that this class will revolve
                              around.

        success_url:          If the form is valid and submitted properly this
                              stores the url that is located after.
    """

    template_name = 'wod/register.html'
    form_class = UserForm
    success_url = '/login/'

    def dispatch(self, *args, **kwargs):
        """Overrides django's dispatch method.

        Args:
            self:              References the class itself.

            *args:             Stores uncertain amount of addition arguments
                               passed.

            **kwargs:          Allows the passing through keyword arguments to
                               provide a variable name as it is passed into
                               this function.
        """

        return super(RegisterView, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        """Overrides django's form_valid method.

        Authenticates users based of their inputted credentials and logs them
        into the site if they are properly authenticated.

        Args:
            self:              References the class itself.

            form:              A reference to the form being processed, in this
                               case AuthenticationForm.

        """

        new_user = User.objects.create_user(**form.cleaned_data)
        new_user.save()

        return super(RegisterView, self).form_valid(form)

    def post(self, request, *args, **kwargs):
        """Overrides django's post method.

        Args:
            self:              References the class itself.

            *args:             Stores uncertain amount of addition arguments
                               passed.

            **kwargs:          Allows the passing through keyword arguments to
                               provide a variable name as it is passed into
                               this function.
        """

        form_class = self.get_form_class()
        form = self.get_form(form_class)

        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class LogoutView(RedirectView):
    """View to processes a user's request to logout of the site.

    Inherits from django's RedirectView class and overrides django's get
    method.

    Attributes:
        template_name:        A field that points to the template this view will
                              render to.

        url:                  Contains the url that the user will be redirected
                              to if they are logged out successfully.
    """

    template_name = 'wod/logout.html'
    url = '/home/'

    def get(self, request, *args, **kwargs):
        logout(self.request)
        return super(LogoutView, self).get(request, *args, **kwargs)
