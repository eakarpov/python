from django.db import models
from datetime import date


class Charge(models.Model):
    date = models.DateField(
        default=date.today()
    )
    value = models.DecimalField(
        max_digits=7,
        decimal_places=2
    )

    def __str__(self):
        return "" + str(self.date) + " " + str(self.value)



