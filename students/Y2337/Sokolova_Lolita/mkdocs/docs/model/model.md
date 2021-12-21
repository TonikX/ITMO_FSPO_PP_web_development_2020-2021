# Создание модели
```python 
class Driver(models.Model):
    name = models.CharField(max_length=45)
    exp_start = models.DateField()


class MotorDepot(models.Model):
    name = models.CharField(max_length=45)
    address = models.CharField(max_length=60)


class Garage(models.Model):
    address = models.CharField(max_length=60)
    motor_depot_id = models.ForeignKey(MotorDepot, on_delete=models.CASCADE, null=True)


class Fuel(models.Model):
    fuel_name = models.CharField(max_length=45)
    liter = models.FloatField()


class Car(models.Model):
    car_model = models.CharField(max_length=45)
    reg_number = models.CharField(max_length=12)
    garage_id = models.ForeignKey(Garage, on_delete=models.SET_NULL, null=True)
    refuels = models.ManyToManyField(to=Fuel, through='Refuel')


class Refuel(models.Model):
    car_id = models.ForeignKey(Car, on_delete=models.SET_NULL, null=True)
    id_fuel = models.ForeignKey(Fuel, on_delete=models.SET_NULL, null=True)
    liters = models.FloatField()


class Waybill(models.Model):
    id_car = models.ForeignKey(Car, on_delete=models.SET_NULL, null=True)
    id_driver = models.ForeignKey(Driver, on_delete=models.SET_NULL, null=True)
    trip_date = models.DateField(default=date.today)

    point_of_loading = models.CharField(max_length=255)
    point_if_unloading = models.CharField(max_length=255)
    mileage_total = models.IntegerField(null=True, blank=True, default=None)
    mileage_cargo = models.IntegerField(null=True, blank=True, default=None)
    consignor = models.CharField(max_length=255)
    consignee = models.CharField(max_length=255)
    order_time = models.FloatField(null=True, blank=True, default=None)

```