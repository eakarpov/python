from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.template.context_processors import csrf
from django.views.decorators.http import require_POST
from django.shortcuts import render_to_response
import sqlite3 as db

from .forms import ChargeForm
from .models import Charge
from .generator import random_transactions


# Create your views here.
def index(request):
    template = loader.get_template('index.html')
    context = RequestContext(request, {
        "title": "Main page"
    })
    return HttpResponse(template.render(context))


def charges(request):
    variables = Charge.objects.all()
    var_pos = []
    for i in range(len(variables)):
        if variables[i].value >= 0:
            var_pos.append(variables[i])
    var_neg = []
    for i in range(len(variables)):
        if variables[i].value < 0:
            var_neg.append(variables[i])
    template = loader.get_template('charges.html')
    var_neg.sort()
    var_pos.sort()
    context = RequestContext(request, {
        "var_pos": var_pos,
        "var_neg": var_neg,
        "title": "Account statement"
    })
    return HttpResponse(template.render(context))


def create_charge(request):
    form = ChargeForm()
    template = loader.get_template('charge_form.html')
    context = RequestContext(request, {
        'title': "My charge form",
        'form': form,
        'info': ""
    })
    return HttpResponse(template.render(context))


def charge_form(request):
    info = ""
    if request.method == 'POST':
        form = ChargeForm(request.POST)
        info = 'Форма заполнена, но некорректна'
        if form.is_valid():
            form.save()
            info = 'Форма заполнена корректно'
    else:
        form = ChargeForm()
    template = loader.get_template('charge_form.html')
    context = RequestContext(request, {
        'title': "My charge form",
        'form': form,
        'info': info
    })
    if request.POST is not None:
        context.update(csrf(request))
    return HttpResponse(template.render(context))


def charge_list(request):
    var_pos = []
    var_neg = []
    for i in range(10):
        date_value, value = next(random_transactions())
        if value < 0:
            var_neg.append((date_value, value))
        else:
            var_pos.append((date_value, value))
    template = loader.get_template('charge_list.html')
    var_pos.sort()
    var_neg.sort()
    context = RequestContext(request, {
        "var_pos": var_pos,
        "var_neg": var_neg,
        "title": "Generated account statement"
    })
    print(var_pos)
    return HttpResponse(template.render(context))

