from django.db import models


class Discipline(models.Model):
    name = models.CharField(max_length=100, null=False, verbose_name="Название", unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Дисциплина"
        verbose_name_plural = "Дисциплины"


class Lecturer(models.Model):
    first_name = models.CharField(max_length=30, null=False, verbose_name="Имя")
    surname = models.CharField(max_length=30, null=False, verbose_name="Фамилия")
    patronymic = models.CharField(max_length=30, null=True, blank=True, verbose_name="Отчество")
    disciplines = models.ManyToManyField(Discipline, verbose_name="Дисциплины")

    def __str__(self):
        return f"{self.surname} {self.first_name} {self.patronymic or ''}"

    class Meta:
        verbose_name = "Преподаватель"
        verbose_name_plural = "Преподаватели"


class Group(models.Model):
    number = models.CharField(max_length=5, null=False, verbose_name="Номер", unique=True)
    students_quantity = models.IntegerField(null=False, verbose_name="Количество студентов")
    disciplines = models.ManyToManyField(Discipline, verbose_name="Дисциплины")

    def __str__(self):
        return self.number

    class Meta:
        verbose_name = "Группа"
        verbose_name_plural = "Группы"


class Audience(models.Model):
    number = models.CharField(max_length=3, null=False, verbose_name="Номер", unique=True)
    aud_type = models.CharField(max_length=30, null=True, blank=True, verbose_name="Тип аудитории")

    def __str__(self):
        return self.number

    class Meta:
        verbose_name = "Аудитория"
        verbose_name_plural = "Аудитории"


class Schedule(models.Model):
    lecturer = models.ForeignKey(Lecturer, on_delete=models.CASCADE, verbose_name="Преподаватель")
    discipline = models.ForeignKey(Discipline, on_delete=models.CASCADE, verbose_name="Дисциплина")
    group = models.ForeignKey(Group, on_delete=models.CASCADE, verbose_name="Группа")
    audience = models.ForeignKey(Audience, on_delete=models.CASCADE, verbose_name="Аудитория")

    DAYS_OF_WEEK = (
        ('Понедельник', 'ПН'),
        ('Вторник',     'ВТ'),
        ('Среда',       'СР'),
        ('Четверг',     'ЧТ'),
        ('Пятница',     'ПТ'),
        ('Суббота',     'СБ'),
    )

    day_of_the_week = models.CharField(max_length=15, choices=DAYS_OF_WEEK, verbose_name="День недели")

    LECTURE_BEGIN = (
        ('8:20',  '1'),
        ('10:00', '2'),
        ('11:40', '3'),
        ('13:30', '4'),
        ('15:20', '5'),
        ('17:00', '6'),
    )

    lecture_begin = models.CharField(max_length=5, choices=LECTURE_BEGIN, verbose_name="Номер пары")

    class Meta:
        verbose_name = "Расписание"
        verbose_name_plural = "Расписание"
