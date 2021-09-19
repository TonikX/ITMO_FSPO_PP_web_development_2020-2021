from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from django.utils.translation import gettext_lazy as _


class ActiveSubstance(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


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

    def __str__(self):
        return self.name


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
    active_substance = models.ForeignKey(ActiveSubstance, on_delete=models.CASCADE)
    packaging = models.IntegerField(choices=PackageType.choices)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_packaging(self):
        return {
            1: "Автоинжектор",
            2: "Ампула",
            3: "Банка",
            4: "Бумага",
            5: "Бутыль",
            6: "Ингалятор",
            7: "Пакет",
            8: "Упаковка контурная ячейковая",
            9: "Флакон",
            10: "Флакон - капельница",
            11: "Шприц"}[self.packaging]


class Unit(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    amount = models.IntegerField(default=1)
    product_date = models.DateField(null=True)
    open_date = models.DateField(null=True, blank=True, default=now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.item.name
