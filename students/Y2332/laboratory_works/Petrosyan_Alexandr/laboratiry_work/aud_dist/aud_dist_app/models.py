from django.db import models


class Discipline(models.Model):
    name = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.name


class Lecturer(models.Model):
    firstname = models.CharField(max_length=30, null=False)
    surname = models.CharField(max_length=30, null=False)
    patronymic = models.CharField(max_length=30, null=True)
    disciplines = models.ManyToManyField(Discipline)

    def __str__(self):
        return f"{self.surname} {self.firstname}"


class Group(models.Model):
    number = models.CharField(max_length=5, null=False)
    students_quantity = models.IntegerField(null=False)
    disciplines = models.ManyToManyField(Discipline)

    def __str__(self):
        return self.number


class Audience(models.Model):
    number = models.CharField(max_length=3, null=False)
    aud_type = models.CharField(max_length=30, null=True)

    def __str__(self):
        return self.number


class Schedule(models.Model):
    lecturer = models.ForeignKey(Lecturer, on_delete=models.DO_NOTHING)
    discipline = models.ForeignKey(Discipline, on_delete=models.DO_NOTHING)
    group = models.ForeignKey(Group, on_delete=models.DO_NOTHING)
    audience = models.ForeignKey(Audience, on_delete=models.DO_NOTHING)

    DAYS_OF_WEEK = (
        ('1', 'Monday'),
        ('2', 'Tuesday'),
        ('3', 'Wednesday'),
        ('4', 'Thursday'),
        ('5', 'Friday'),
        ('6', 'Saturday'),
        ('7', 'Sunday'),
    )

    day_of_the_week = models.CharField(max_length=10, choices=DAYS_OF_WEEK)

    BEGIN_TIME = (
        ('1', '8:20'),
        ('2', '10:00'),
        ('3', '11:40'),
        ('4', '13:30'),
        ('5', '15:20'),
        ('6', '17:00'),
    )

    begin_time = models.CharField(max_length=5, choices=BEGIN_TIME)
