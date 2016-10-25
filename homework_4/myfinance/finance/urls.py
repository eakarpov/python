from django.conf.urls import url
from finance.views import index
from finance.views import charges
from finance.views import charge_list
from finance.views import charge_form
from finance.views import create_charge


urlpatterns = [
    url(r'^$', index, name="index"),
    url(r'^charges/$', charges, name="charges"),
    url(r'^charge_list/$', charge_list, name="charge_list"),
    url(r'^create_charge/$', create_charge, name="create_charge"),
    url(r'^charge_form/$', charge_form, name="charge_form")
]