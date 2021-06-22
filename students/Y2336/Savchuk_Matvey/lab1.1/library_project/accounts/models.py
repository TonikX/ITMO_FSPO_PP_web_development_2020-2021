from django.db import models

# Create your models here.


class Customer(models.Model):
	name = models.CharField(max_length=200, null=True)
	phone = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200, null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self):
		return self.name


class Book(models.Model):
	CATEGORY = (
			('Копирайтинг', 'Копирайтинг'),
			('Маркетинг', 'Маркетинг'),
			('Базы данных', 'Базы данных'),
			)

	name = models.CharField(max_length=200, null=True)
	price = models.FloatField(null=True)
	category = models.CharField(max_length=200, null=True, choices=CATEGORY)
	description = models.CharField(max_length=200, null=True, blank=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self):
		return self.name


class Order(models.Model):
	STATUS = (
			('В ожидании', 'В ожидании'),
			('Заказ отменен', 'Заказ отменен'),
			('Выполнено', 'Выполнено'),
			)

	customer = models.ForeignKey(Customer, null=True, on_delete= models.SET_NULL)
	book = models.ForeignKey(Book, null=True, on_delete= models.SET_NULL)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	status = models.CharField(max_length=200, null=True, choices=STATUS)
	note = models.CharField(max_length=1000, null=True)

	def __str__(self):
		return self.book.name
