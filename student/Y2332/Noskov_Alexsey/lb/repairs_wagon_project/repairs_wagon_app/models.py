from django.db import models
from django.contrib.auth.models import AbstractUser


# On 1234

class Wagon(models.Model):
    reg_number = models.IntegerField(unique=True)
    reg_name = models.CharField(max_length=60, unique=True)
    reg_chief = models.CharField(max_length=20, unique=True)
    type = models.CharField(max_length=30)
    type_year = models.IntegerField()
    dop_number = models.IntegerField()
    ralway_addressExternal = models.CharField(max_length=80)

    def __str__(self):
        return "{} {} {} {} {} {}".format(self.reg_number, self.reg_name, self.reg_chief, self.type, self.type_year,
                                          self.dop_number)


class RepairBrigade(models.Model):
    bonus_persent = models.IntegerField()
    fio_chief = models.CharField(max_length=30)


class Schedule_works(models.Model):
    data = models.IntegerField()
    work_shift = models.CharField(max_length=10)
    repair_brigade = models.ForeignKey(RepairBrigade, on_delete=models.CASCADE)


class Repair(models.Model):
    resalt = models.CharField(max_length=10, unique=True)
    reason = models.CharField(max_length=100)
    cost = models.IntegerField(unique=True)
    day_start = models.DateTimeField()
    day_stop = models.DateTimeField()
    type_repair = models.CharField(max_length=15)
    schedule = models.ForeignKey(Schedule_works, default=1, on_delete=models.CASCADE)
    wagon = models.ForeignKey(Wagon, on_delete=models.CASCADE)

    def __str__(self):
        return "{} {} {} {} {} {} {}".format(self.resalt, self.reason, self.cost, self.day_start, self.day_stop,
                                             self.type_repair, self.schedule)


class Worker(AbstractUser):
    REQUIRED_FIELDS = []
    tab_number = models.IntegerField(unique=True, null=True)
    fio_worker = models.CharField(max_length=30, null=True)
    year_worker = models.IntegerField(null=True)
    base_worker = models.CharField(max_length=50, null=True)
    bonus_worker = models.IntegerField(default=5, null=True)
    number_cart_bank = models.IntegerField(unique=True, null=True)
    brigade = models.ManyToManyField(RepairBrigade, default=1, related_name='workers', null=True)

    def __str__(self):
        return "{} {} {} {} {} {} {} {}".format(self.username, self.password, self.tab_number, self.fio_worker,
                                                self.year_worker, self.base_worker,
                                                self.bonus_worker, self.number_cart_bank)


class Depo(models.Model):
    address_depo = models.CharField(max_length=80, unique=True)
    ur_address_depo = models.CharField(max_length=80, unique=True)


class employment_contract(models.Model):
    day_start = models.DateTimeField()
    day_stop = models.DateTimeField()
    type = models.CharField(max_length=15)
    position = models.CharField(max_length=20)
    salary = models.IntegerField()
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)
    depo = models.ForeignKey(Depo, on_delete=models.CASCADE)
