from django.db import models


class Car(models.Model):
    gos_number = models.CharField(max_length=15)
    mark = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    color = models.CharField(max_length=30)


def __str__(self):
    return "{} {}".format(self.gos_number, self.mark, self.model, self.color)


class CarOwner(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateTimeField(blank=True, null=True)
    cars = models.ManyToManyField(Car, through='Own')


def __str__(self):
    return "{} {}".format(self.first_name, self.last_name, self.birth_date, self.cars)


class Own(models.Model):
    date_start = models.DateTimeField()
    date_finish = models.DateTimeField(blank=True, null=True)
    id_carOwner = models.ForeignKey(CarOwner, on_delete=models.CASCADE)
    id_car = models.ForeignKey(Car, on_delete=models.CASCADE)


def __str__(self):
    return "{} {}".format(self.date_start, self.date_finish, self.id_carOwner, self.id_car)


class Doc(models.Model):
    id_carOwner = models.ForeignKey(CarOwner, on_delete=models.CASCADE)
    doc_num = models.CharField(max_length=10)
    type = models.CharField(max_length=10)
    date_issue = models.DateTimeField(blank=True, null=True)


def __str__(self):
    return "{} {}".format(self.id_carOwner, self.doc_num, self.type, self.date_issue)
