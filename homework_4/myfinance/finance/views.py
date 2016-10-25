from django.template import RequestContext, loader
from django.template.context_processors import csrf
from django.http import HttpResponse
from django.views.generic import TemplateView

from .forms import ChargeForm
from .models import Charge
from .generator import random_transactions


# Create your views here.
class MainView(TemplateView):
    template_name = 'index.html'

    def __init__(self):
        self.template = loader.get_template(template_name=self.template_name)

    def get(self, request, *args, **kwargs):
        context = RequestContext(request, {
            "title": "Main page"
        })
        return HttpResponse(self.template.render(context))


class ChargeFromModelView(TemplateView):
    template_name = 'charges.html'

    def __init__(self):
        self.variables = Charge.objects.all()
        self.template = loader.get_template(template_name=self.template_name)
        self.var_pos = []
        self.var_neg = []
        for i in range(len(self.variables)):
            if self.variables[i].value >= 0:
                self.var_pos.append(self.variables[i])
        for i in range(len(self.variables)):
            if self.variables[i].value < 0:
                self.var_neg.append(self.variables[i])
        self.var_pos.sort(key=lambda el: el.date)
        self.var_neg.sort(key=lambda el: el.date)

    def get(self, request, *args, **kwargs):
        context = RequestContext(request, {
            "var_pos": self.var_pos,
            "var_neg": self.var_neg,
            "title": "Account statement"
        })
        return HttpResponse(self.template.render(context))


class ChargeFormView(TemplateView):
    template_name = 'charge_form.html'

    def __init__(self):
        self.info = []
        self.form = ChargeForm()
        self.template = loader.get_template(template_name=self.template_name)

    # I have made this to prevent a csrf mistake...
    def post(self, request):
        return self.get(request)

    def get(self, request, *args, **kwarg):
        if request.method == 'POST':
            form = ChargeForm(request.POST)
            self.info.append("Form is filled but is not correct")
            if form.is_valid():
                form.save()
                self.info.clear()
                self.info.append("Form has been validated")
                self.info.append("You added new charge (" + str(request.POST.get('date')) + ", " +
                                 str(request.POST.get('value')) + ")")
                form = ChargeForm()
        else:
            form = ChargeForm()
        context = RequestContext(request, {
            'title': "My charge form",
            'form': form,
            'info': self.info
        })
        if request.POST is not None:
            context.update(csrf(request))
        return HttpResponse(self.template.render(context))


class ChargeFromGeneratorView(TemplateView):
    template_name = 'charge_list.html'

    def __init__(self):
        self.var_pos = []
        self.var_neg = []
        self.template = loader.get_template(template_name=self.template_name)
        for (date_value, value) in random_transactions():
            if value < 0:
                self.var_neg.append((date_value, value))
            else:
                self.var_pos.append((date_value, value))
        self.var_pos.sort()
        self.var_neg.sort()

    def get(self, request, *args, **kwargs):
        context = RequestContext(request, {
            "var_pos": self.var_pos,
            "var_neg": self.var_neg,
            "title": "Generated account statement"
        })
        return HttpResponse(self.template.render(context))


