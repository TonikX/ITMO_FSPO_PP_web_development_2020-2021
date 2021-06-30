from django.db import models

class auto(models.Model):
    state_number = models.CharField(max_length = 15)
    mark = models.CharField(max_length = 20)
    model = models.CharField(max_length = 20)
    color = models.CharField(max_length = 30, null = True)


class car_owner(models.Model):
    Surname = models.CharField(max_length = 30)
    Name = models.CharField(max_length = 30)
    Date_of_Birth = models.DateTimeField(null = True)
    car_ownerships = models.ManyToManyField(auto, through = 'car_ownership')


class car_ownership(models.Model):
    car_owner_id = models.ForeignKey(car_owner, on_delete = models.CASCADE, null = True)
    auto_id = models.ForeignKey(auto, on_delete = models.CASCADE, null = True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(null = True)


class driver_license(models.Model):
    car_owner_id = models.ForeignKey(car_owner, on_delete = models.CASCADE)
    driver_license_id = models.CharField(max_length = 10)
    type = models.CharField(max_length = 10)
    date_of_receipt = models.DateTimeField()