from django.db import models
from datetime import datetime

# Продукция:
# Номер продукции, название,
# единица измерения,
# цена, количество,
# минимальное количество,
# описание


class Production(models.Model):
    code = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    unit = models.CharField(max_length=50, blank=True, null=True)
    amount = models.BigIntegerField()
    minimum = models.BigIntegerField()
    desc = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return '%s %s %s' % (self.code, self.name, self.desc)

# Поставщик:
# номер поставщика,
# имя, адрес


class Supplier(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)

    def __str__(self):
        return '%s' % self.name

# Сотрудник:
# номер сотрудника,
# имя,
# паспортные данные


class Employer(models.Model):
    code = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=50)
    pass_data = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return '%s' % self.name

# Клиент:
# номер клиента,
# имя, номер аккаунта,
# адрес


class Client(models.Model):
    name = models.CharField(max_length=50)
    acc_num = models.CharField(max_length=100, unique=True)
    address = models.CharField(max_length=50)

    def __str__(self):
        return '%s' % self.name

# Заказ содержит информацию о клиенте, поставщике, сотруднике, товаре,
# а также дату поставки и вывоза, цену, количество и статус заказа


class Batch(models.Model):
    supplier = models.ForeignKey('Supplier', on_delete=models.CASCADE)
    client = models.ForeignKey('Client', on_delete=models.CASCADE)
    employer = models.ForeignKey('Employer', on_delete=models.CASCADE)
    production = models.ForeignKey('Production', on_delete=models.CASCADE)
    supply_date = models.DateField(default=datetime.now())
    delivery_date = models.DateField()
    amount = models.BigIntegerField()
    price = models.BigIntegerField()
    isFulfilled = models.BooleanField(default=False)

    db_constraints = {
        'price_rule': 'check (price > 0)',
    }

    def __str__(self):
        return '%s %s %s %s' % (self.supplier, self.client, self.employer, self.production)
