from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

import hello.views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gettingstarted.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', hello.views.main, name='main'),
    url(r'^index', hello.views.main, name='main'),
    url(r'^about', hello.views.about, name='main'),
    url(r'^blog', hello.views.blog, name='main'),
    url(r'^contact', hello.views.contact, name='main'),
    url(r'^details', hello.views.details, name='main'),
    url(r'^login', hello.views.login, name='main'),
    url(r'^products', hello.views.products, name='main'),
    url(r'^register', hello.views.register, name='main'),
    url(r'^main', hello.views.index, name='index'),
    #url(r'^db', hello.views.db, name='db'),
    url(r'^admin/', include(admin.site.urls)),

)
