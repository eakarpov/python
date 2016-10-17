from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

from .models import Charge


# Create your views here.
def index(request):
    template = loader.get_template('index.html')
    context = RequestContext(request, {
        "title": "Main page"
    })
    return HttpResponse(template.render(context))


def charges(request):
    variables = Charge.objects.all()
    choices = dict(Charge.CURRENCY_LIST)
    for var in variables:
        var.currency = choices.get(var.currency)
    template = loader.get_template('charges.html')
    context = RequestContext(request, {
        "vars": variables,
        "title": "Account statement"
    })
    return HttpResponse(template.render(context))
