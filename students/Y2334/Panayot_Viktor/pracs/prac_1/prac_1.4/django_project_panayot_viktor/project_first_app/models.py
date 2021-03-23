from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model

class auto(models.Model):
    state_number = models.CharField(max_length = 15)
    mark = models.CharField(max_length = 20)
    model = models.CharField(max_length = 20)
    color = models.CharField(max_length = 30, null = True)
    
    def __str__(self):
	    return "{} {}".format(self.state_number, self.mark, self.model, self.color)


class CarOwner(AbstractUser):
    Surname = models.CharField(max_length = 30, blank = True)
    Name = models.CharField(max_length = 30, blank = True)
    Date_of_Birth = models.DateTimeField(null = True, blank = True)
    passport_number = models.CharField(blank = True, max_length = 30);
    home_adress = models.CharField(blank = True, null = True, max_length = 100)
    citizenship = models.CharField(blank = True, max_length = 30)
    CarOwnerships = models.ManyToManyField(auto, through = 'CarOwnership')


Car_Owner = get_user_model()


class CarOwnership(models.Model):
    CarOwner_id = models.ForeignKey(Car_Owner, on_delete = models.CASCADE, null = True)
    auto_id = models.ForeignKey(auto, on_delete = models.CASCADE, null = True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(null = True)
    
    def __str__(self):
	    return "{} {}".format(self.auto_id, self.CarOwner_id, self.end_date)


class driver_license(models.Model):
    CarOwner_id = models.ForeignKey(Car_Owner, on_delete = models.CASCADE)
    driver_license_id = models.CharField(max_length = 10)
    type = models.CharField(max_length = 10)
    date_of_receipt = models.DateTimeField()
