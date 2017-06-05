from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import urls
from pages.views import home, demo_list, home_ch
from report.views import result

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^home_ch', home_ch, name='home_ch'),
    url(r'^demo_list$', demo_list, name='demo_list'),
    url(r'^report/', include('report.urls')),
    url(r'^accounts/', include(urls)),
    url(r'^admin/', include(admin.site.urls)),
]
