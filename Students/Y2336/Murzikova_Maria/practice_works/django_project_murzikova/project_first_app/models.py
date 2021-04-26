from django.db import models

# Create your models here.
class Owner(models.Model):
    surname = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    bDay = models.DateField()
    def __str__(self):
        return "{} {} {}".format(self.pk, self.surname, self.name)

class Car(models.Model):
    number = models.CharField(max_length=15)
    mark = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    color = models.CharField(max_length=30)
    owner = models.ManyToManyField(Owner, through='Hold')
    def __str__(self):
        return "{} {}".format(self.mark, self.model)

class Hold(models.Model):
    id_owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    id_car = models.ForeignKey(Car, on_delete=models.CASCADE)
    startDate = models.DateField()
    endDate = models.DateField()
    def __str__(self):
        return "{} {}".format(self.id_owner, self.id_car)

class License(models.Model):
    id_owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    licenseNumber = models.CharField(max_length=10)
    type = models.CharField(max_length=10)
    issueDate = models.DateField()
    def __str__(self):
        return self.licenseNumber