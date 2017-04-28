from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^result/', views.result, name='result'),
    # url(r'^detail/(?P<pk>[0-9]+)/$', views.detail, name='detail'),
]
