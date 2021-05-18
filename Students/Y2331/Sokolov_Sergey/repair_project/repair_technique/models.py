from django.db import models
from django.contrib.auth.models import AbstractUser


class Manager(AbstractUser):
    name = models.CharField(max_length=20, blank=True, null=True)


class Customer(models.Model):
    customer_telephone = models.CharField(max_length=45)
    customer_type = models.CharField(max_length=45)
    representative_full_name = models.CharField(max_length=45)
    supervisor_full_name = models.CharField(max_length=45)
    customer_inn = models.CharField(max_length=45)
    customer_address = models.CharField(max_length=45)
    customer_distinct = models.CharField(max_length=45)
    customer_account_number = models.CharField(max_length=45)

    def __str__(self):
        return self.representative_full_name


class ModelTechnique(models.Model):
    brand_technique = models.CharField(max_length=45)
    type_technique = models.CharField(max_length=45)
    manufacturer_technique = models.CharField(max_length=45)

    def __str__(self):
        return self.type_technique + '-' + self.brand_technique


class Technique(models.Model):
    model_technique = models.ForeignKey(ModelTechnique, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date_create = models.DateField(null=True)
    date_end_guarantee = models.DateField(null=True)
    technique_photo = models.ImageField

    def __str__(self):
        return str(self.id) + '-' + str(self.model_technique)


class PriceList(models.Model):
    name_service = models.CharField(max_length=45)
    price = models.IntegerField()

    def __str__(self):
        return self.name_service


class Master(models.Model):
    master_full_name = models.CharField(max_length=45)
    insurance_number = models.CharField(max_length=45)
    master_phone = models.CharField(max_length=45)
    master_passport = models.CharField(max_length=45)
    master_qualification = models.CharField(max_length=45)
    work_experience = models.IntegerField()
    sum_amount_fine = models.IntegerField()

    def __str__(self):
        return self.master_full_name


class Order(models.Model):
    technique = models.ForeignKey(Technique, on_delete=models.CASCADE)
    master = models.ForeignKey(Master, on_delete=models.CASCADE)
    price_list = models.ForeignKey(PriceList, on_delete=models.CASCADE)
    status_execution = models.CharField(max_length=45)
    status_guilt = models.CharField(max_length=45)
    note = models.CharField(max_length=45)
    date_receipt = models.DateTimeField
