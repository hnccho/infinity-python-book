from django.conf.urls import patterns, include, url
from mysite.views import hello
from calc.views import add

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    url(r'^hello/', hello),
    url(r'^calc/add$', add),

    url(r'^admin/', include(admin.site.urls)),
)
