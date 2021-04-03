from django.db import models


class Car(models.Model):
    gos_number = models.CharField(max_length=15)
    mark = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    color = models.CharField(max_length=30)

    def __str__(self):
        return "{}, {}, {}, {}".format(self.gos_number, self.mark, self.model, self.color)


class CarOwner(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_day = models.DateTimeField(blank=True)
    cars = models.ManyToManyField(Car, through='Own')

    def __str__(self):
        return "{}, {}, {}".format(self.first_name, self.last_name, self.birth_day)


class Own(models.Model):
    date_start = models.DateTimeField()
    date_end = models.DateTimeField(blank=True)
    id_CarOwner = models.ForeignKey(CarOwner, on_delete=models.CASCADE)
    id_Car = models.ForeignKey(Car, on_delete=models.CASCADE)


class Doc(models.Model):
    id_CarOwner = models.ForeignKey(CarOwner, on_delete=models.CASCADE)
    doc_num = models.CharField(max_length=10)
    type = models.CharField(max_length=10)
    date_issue = models.DateTimeField()
