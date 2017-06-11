# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from django.contrib import admin

from rest_framework import routers



urlpatterns = [
    # Examples:
    # url(r'^$', 'Gourmery.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')), 

    url(r'^adminCre8215&11/', include(admin.site.urls)),
    url(r'^token_auth/$','rest_framework.authtoken.views.obtain_auth_token'),

    #API
    url(r'^hello/','API.views.hello_world',name='hello'),
    url(r'^api/getUserInfo','API.views.getUserInfo',name='getUserInfo'),
    url(r'^api/getUserPayment','API.views.getUserPayment',name='getUserPayment'),
    url(r'^api/getUserGustos','API.views.getUserGustos',name='getUserGustos'),
    url(r'^api/getUserCustomers','API.views.getUserCustomers',name='getUserCustomers'),
    url(r'^api/getUserCurrentOrder','API.views.getUserCurrentOrder',name='getUserCurrentOrder'),
    url(r'^api/getUserOrders','API.views.getUserOrders',name='getUserOrders'),
    url(r'^api/getSucursales','API.views.getSucursales',name='getSucursales'),

]
