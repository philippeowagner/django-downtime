from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/$', TemplateView.as_view(template_name='hello.html')),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', name='auth_login'),

)
