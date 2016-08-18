"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include, patterns
from django.contrib import admin
admin.autodiscover()
from app.views import math, welcome, set_cookie, get_cookie, login, index, logout
from restaurants.views import menu, meta, list_restaurants, comment


urlpatterns = [
    #url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/', admin.site.urls),
    #url(r'^here/', here),
    #url(r'^(\d{1,2})/math/(\d{1,2})/', math),
    url(r'^menu/(\d{1,5})/', menu),
    url(r'^meta/', meta),
    url(r'^welcome/', welcome),
    url(r'^restaurants_list/', list_restaurants),
    url(r'^comment/(\d{1,5})/', comment),
    url(r'^set_c/', set_cookie),
    url(r'^get_c/', get_cookie),
    url(r'^index/', index),
    url(r'^login/', login),
    url(r'^logout/', logout),
]
