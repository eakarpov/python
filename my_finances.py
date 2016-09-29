from decimal import Decimal


def rounder(getter):
    def wrapper(self):
        x = getter(self)
        result = round(x, 2)
        return result
    return wrapper


class Charge:
    def __init__(self, value):
        self._value = Decimal(value)

    def __str__(self):
        return str(self.get_value)

    @property
    @rounder
    def get_value(self):
        return self._value


class Account:
    def __init__(self, value=0):
        self._charges = []
        self._total = Decimal(value)
        self._current = 0

    def __iter__(self):
        return iter(self._charges)

    def __next__(self):
        if self._current > len(self._charges):
            self._current = 0
            raise StopIteration
        result = self._current
        self._current += 1
        return result

    @rounder
    def get_total(self):
        return self._total

    """Deposits your money on your account."""
    def deposit(self, value):
        self._total += Decimal(value)
        self._charges.append(Charge(value))

    """Withdraws your money from your account."""
    def withdraw(self, value):
        if self._total - Decimal(value) >= 0:
            self._total -= Decimal(value)
            self._charges.append(Charge(-value))
        else:
            print("Negative profit is unavailable!")


if __name__ == '__main__':
    acc = Account()
    for i in [1.0001, 1.4455]:
        acc.deposit(i)
    for i in acc:
        print('%s' % i)
    print(acc.get_total())
    acc.withdraw(2.4457)
    print(acc.get_total())
