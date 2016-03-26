from django.conf.urls import include, url
from django.contrib import admin
from wod.views import LoginView

urlpatterns = [
    # Examples:
    # url(r'^$', 'project_worthy.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'home/', include('core.urls')),
    url(r'wod/', include('wod.urls')),
    url(r'^login/', LoginView.as_view(), name="login"),
    url(r'^admin/', include(admin.site.urls)),
]
