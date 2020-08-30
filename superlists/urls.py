from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from lists import views as list_views, urls as list_urls


urlpatterns = [
    url(r'^$', list_views.home_page, name='home'),
    url(r'^lists/', include(list_urls)),
]
