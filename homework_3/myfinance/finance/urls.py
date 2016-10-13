from django.conf.urls import url
from finance.views import index
from finance.views import charges

urlpatterns = [
    url(r'^$', index),
    url(r'^charges/$', charges)
]