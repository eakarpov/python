from django.forms import ModelForm, fields, widgets
from django.core.exceptions import ValidationError
from datetime import date
from django.forms.models import model_to_dict
from django.shortcuts import get_object_or_404

from .models import Charge


class ChargeForm(ModelForm):

    class Meta:
        model = Charge
        fields = [
            'date',
            'value'
        ]

    def clean(self):
        value = self.cleaned_data.get('value')
        date_value = self.cleaned_data.get('date')
        if value < 0:
            if date_value > date.today():
                raise ValidationError('You can not withdraw from the account on the future dates!')
        if value == 0:
            raise ValidationError('You can not add a without money charge!')
        return self.cleaned_data
