"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from website.views import hello, current_datetime, hours_ahead,hello_world,homepage_view,display_meta
from books import views
from equations import views as eviews

urlpatterns = [
	url(r'^$', homepage_view),
    url(r'^admin/', admin.site.urls),
	url(r'^hello/$', hello_world),
	url(r'^time/$', current_datetime), 
	url(r'^time/plus/(\d{1,2})/$', hours_ahead),
	url(r'^search-form/$', views.search_form),
	url(r'^search/$', views.search),
    url(r'^meta/$', display_meta),
    url(r'^printall/$', views.printall),
    url(r'^rk/', eviews.RKindex),
    url(r'^RungeKutta/', eviews.RungeKutta),
	url(r'^simple/$', eviews.simple,name="simple"),
]
