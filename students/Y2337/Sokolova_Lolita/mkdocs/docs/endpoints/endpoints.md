# Endpoints

## ``` /drivers/ ```

Методы:

* get - получить список водителей
* post - создать водителя (name, exp_start)
![](1.png)

## ``` /drivers/:id/ ```
Методы:

* get - получить водителя
* put - изменить водителя (name, exp_start)
* patch - изменить водителя (name, exp_start) - опционально
* delete - удалить водителя
![](2.png)

## ``` /motor-depots/ ```
Методы:

* get - получить список автобаз
* post - создать автобазу (name, address)
![](3.png)

## ``` /motor-depots/:id/ ```
Методы:

* get - получить автобазу
* put - изменить автобазу (name, address)
* patch - изменить автобазу (name, address) - опционально
* delete - удалить автобазу
![](4.png)

## ``` /garages/ ```
Методы:

* get - получить список гаражей
* post - создать гараж (address, motor_depot_id)
![](5.png)
## ``` /garages/:id/ ```
Методы:

* get - получить гараж
* put - изменить гараж (address, motor_depot_id)
* patch - изменить гараж (address, motor_depot_id) - опционально
* delete - удалить гараж
![](6.png)

## ``` /cars/ ```
Методы:

* get - получить список машин
* post - создать машину (car_model, reg_number, garage_id, refuels)
![](7.png)

## ``` /cars/:id/ ```
Методы:

* get - получить машину
* put - изменить машину (car_model, reg_number, garage_id, refuels)
* patch - изменить машину (car_model, reg_number, garage_id, refuels) - опционально
* delete - удалить машину
![](8.png)


## ``` /fuels/ ```
Методы:

* get - получить список топлива
* post - создать топливо (fuel_name, liter)
![](9.png)

## ``` /fuels/:id/ ```
Методы:

* get - получить топливо
* put - изменить топливо (fuel_name, liter)
* patch - изменить топливо (fuel_name, liter) - опционально
* delete - удалить топливо
![](10.png)


## ``` /waybills/ ```
Методы:

* get - получить список поездок
* post - создать поездку (id_car, id_driver, trip_date, point_of_loading, point_of_unloading, mileage_total, mileage_cargo, consignor, consignee, order_time)
![](11.png)
## ``` /waybills/:id/ ```
Методы:

* get - получить поездку
* put - изменить поездку (id_car, id_driver, trip_date, point_of_loading, point_of_unloading, mileage_total, mileage_cargo, consignor, consignee, order_time)
* delete - удалить поездку
![](12.png)

## ``` /refuels/ ```
Методы:

* get - получить список заправок
* post - создать заправку (car_id, id_fuel, liters)
![](13.png)

## ``` /refuels/:id/ ```
Методы:

* get - получить заправку
* put - изменить заправку (car_id, id_fuel, liters)
* delete - удалить заправку
![](14.png)
