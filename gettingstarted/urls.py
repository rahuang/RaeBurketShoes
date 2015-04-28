from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

import hello.views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gettingstarted.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', hello.views.landing, name='landing'),
    url(r'^index', hello.views.main, name='index'),
    url(r'^about', hello.views.about, name='about'),
    url(r'^blog', hello.views.blog, name='blog'),
    url(r'^contact', hello.views.contact, name='contact'),
    url(r'^details', hello.views.details, name='details'),
    url(r'^login', hello.views.login, name='login'),
    url(r'^products', hello.views.products, name='products'),
    url(r'^register', hello.views.register, name='register'),
    url(r'^cart', hello.views.cart, name='cart'),
    url(r'^gettogive', hello.views.getToGive, name='gettogive'),
    url(r'^db', hello.views.db, name='db'),
    url(r'^main', hello.views.index, name='index'),
    url(r'^test', hello.views.test, name='main'),
    url(r'^admin/', include(admin.site.urls)),

)
