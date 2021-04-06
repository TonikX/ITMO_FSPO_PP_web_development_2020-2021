from django.db import models as m

class AutoOwner(m.Model):
    name = m.CharField(max_length=30, null=False)
    last_name = m.CharField(max_length=30, null=False)
    birthday_date = m.DateTimeField(null=False)

class Auto(m.Model):
    number = m.CharField(max_length=15, null=False)
    brand = m.CharField(max_length=20, null=False)
    model = m.CharField(max_length=20, null=False)
    color = m.CharField(max_length=30, null=False)

class Owning(m.Model):
    auto_owner = m.ForeignKey(AutoOwner, on_delete=m.CASCADE)
    auto = m.ForeignKey(Auto, on_delete=m.CASCADE)
    start_date = m.DateTimeField(null=False)
    end_date = m.DateTimeField(null=False)

class Paper(m.Model):
    auto_owner = m.ForeignKey(AutoOwner, on_delete=m.CASCADE)
    number = m.CharField(max_length=10, null=False)
    type = m.CharField(max_length=10, null=False)
    date = m.DateTimeField(null=False)

