from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^quzpage', views.quzpage, name='quzpage'),
    # url(r'^detail/(?P<pk>[0-9]+)/$', views.detail, name='detail'),
]
