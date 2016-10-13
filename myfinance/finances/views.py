from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader


# Create your views here.
def index(request):
    template = loader.get_template('index.html')
    context = RequestContext(request, {

    })
    return HttpResponse(template.render(context))


def charges(request):
    template = loader.get_template('charges.html')
    context = RequestContext(request, {

    })
    return HttpResponse(template.render(context))