from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import urls
from pages.views import home_en, demo_list, home_ch
from report.views import result
from tform.views import quzpage

urlpatterns = [
    url(r'^$', home_ch, name='home_ch'),
    url(r'^home_en', home_en, name='home_en'),
    url(r'^demo_list$', demo_list, name='demo_list'),
    url(r'^tform/', include('tform.urls')),
    url(r'^report/', include('report.urls')),
    url(r'^accounts/', include(urls)),
    url(r'^admin/', include(admin.site.urls)),
]
