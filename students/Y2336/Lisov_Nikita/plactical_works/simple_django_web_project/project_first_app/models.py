from django.db import models

# Create your models here.
class Owner(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birth_date = models.DateTimeField(null=True)


class License(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    num = models.CharField(max_length=10)
    type = models.CharField(max_length=10)
    issue_date = models.DateTimeField()

class Auto(models.Model):
    gos_num = models.CharField(max_length=15)
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    color = models.CharField(max_length=30, null=True)

class Ownership(models.Model):
    owners = models.ManyToManyField(Owner)
    autos = models.ManyToManyField(Auto)
    date_start = models.DateTimeField()
    date_end = models.DateTimeField(null=True)

class ExampleModel(models.Model):
    title = models.CharField(max_length = 200)
    description = models.TextField()
    def __str__(self):
        return self.title

class Publisher(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birthdate = models.DateField()

    def __str__(self):
	       return "{} {}".format(self.first_name, self.last_name)

class Book(models.Model):
  name = models.CharField(max_length=100)
  desc = models.CharField(max_length=200)
  publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)

  def __str__(self):
      return "{}, {}".format(self.name, self.publisher)
