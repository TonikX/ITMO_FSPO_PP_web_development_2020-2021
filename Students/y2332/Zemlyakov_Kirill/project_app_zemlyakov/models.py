from django.db import models


# Create your models here.

# database "participation in exhibition"
# table Car Owner
class CarOwner(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birth_date=models.DateField(default="NULL")

    def __str__(self):
        return "{} {} {}".format(self.first_name, self.last_name, self.birth_date)
# table Car
class Car(models.Model):
    license_plate_number=models.CharField(max_length=15)
    car_brand=models.CharField(max_length=20)
    car_model=models.CharField(max_length=20)
    car_color=models.CharField(max_length=30,default="NULL")
    ownerships=models.ManyToManyField(CarOwner,through='Ownership')

    def __str__(self):
        return "{} {} {} {}".format(self.license_plate_number,self.car_brand, self.car_model, self.car_color)
# table Ownership
class Ownership(models.Model):
    owner_car=models.ForeignKey(CarOwner,on_delete=models.CASCADE)
    car_id=models.ForeignKey(Car,on_delete=models.CASCADE)
    start_date=models.DateField()
    end_date=models.DateField(default="NULL")

    def __str__(self):
        return "{} {} {} {}".format(self.owner_car, self.car_id,self.start_date,self.end_date)
# table Driver License
class DriverLicense(models.Model):
    license_num=models.CharField(max_length=10)
    license_type=models.CharField(max_length=10)
    date_of_issue=models.DateField()
    owner_id=models.ForeignKey(CarOwner,on_delete=models.CASCADE)

    def __str__(self):
        return "{} {} {} {}".format(self.license_num, self.license_type, self.date_of_issue, self.owner_id)
