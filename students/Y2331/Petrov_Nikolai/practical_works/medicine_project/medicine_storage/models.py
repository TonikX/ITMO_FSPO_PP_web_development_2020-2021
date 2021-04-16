from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from django.utils.translation import gettext_lazy as _


class ActiveSubstance(models.Model):
    name = models.CharField(max_length=250)


class Manufacturer(models.Model):
    class Country(models.TextChoices):
        RUSSIA = "RU", _("Россия")
        USA = "USA", _("США")

    name = models.CharField(max_length=200)
    country = models.CharField(
        max_length=4,
        choices=Country.choices,
        default=Country.RUSSIA,
    )


class Conditions(models.Model):
    conditions = models.JSONField()


class Item(models.Model):
    class PackageType(models.IntegerChoices):
        AUTOINJECTOR = 1, _("Автоинжектор")
        AMPOULE = 2, _("Ампула")
        BANK = 3, _("Банка")
        PAPER = 4, _("Бумага")
        BOTTLE = 5, _("Бутыль")
        INHALER = 6, _("Ингалятор")
        PACKAGE = 7, _("Пакет")
        BLISTER = 8, _("Упаковка контурная ячейковая")
        VIAL = 9, _("Флакон")
        DROPPER_VIAL = 10, _("Флакон - капельница")
        SYRINGE = 11, _("Шприц")

    name = models.CharField(max_length=200)
    active_substance = models.ForeignKey(ActiveSubstance, on_delete=models.DO_NOTHING)
    packaging = models.IntegerField(choices=PackageType.choices)
    conditions = models.ManyToManyField(Conditions)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.DO_NOTHING)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)


class Unit(models.Model):
    item = models.ForeignKey(Item, on_delete=models.DO_NOTHING)
    amount = models.IntegerField(default=1)
    product_date = models.DateField(null=True)
    open_date = models.DateField(null=True, default=now)
