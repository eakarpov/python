from django.conf.urls import url
from finance.views import MainView
from finance.views import ChargeFormView
from finance.views import ChargeFromGeneratorView
from finance.views import ChargeFromModelView


urlpatterns = [
    url(r'^$', MainView.as_view(), name="index"),
    url(r'^charges/$', ChargeFromModelView.as_view(), name="charges"),
    url(r'^charge_list/$', ChargeFromGeneratorView.as_view(), name="charge_list"),
    url(r'^charge_form/$', ChargeFormView.as_view(), name="charge_form")
]