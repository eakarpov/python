from django.conf.urls import url
from finances.views import index
from finances.views import charges

urlpatterns = [
    url(r'^$', index),
    url(r'^charges/$', charges)
]