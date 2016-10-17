from django.db import models


class Charge(models.Model):
    CURRENCY_LIST = (
        ('rub', 'Rubles'),
        ('usd', 'Dollars'),
        ('eu', 'Euros')
    )
    date = models.DateField()
    amount = models.DecimalField(
        max_digits=7,
        decimal_places=2
    )
    currency = models.CharField(
        max_length=3,
        choices=CURRENCY_LIST,
        default='rub'
    )

    def __str__(self):
        return "" + str(self.date) + " " + str(self.amount) + " " + str(self.currency)
