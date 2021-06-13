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
        (1, 'Понедельник',),
        (2, 'Вторник'),
        (3, 'Среда'),
        (4, 'Четверг'),
        (5, 'Пятница'),
        (6, 'Суббота'),
    )

    day_of_the_week = models.IntegerField(choices=DAYS_OF_WEEK, verbose_name="День недели")

    LECTURE_BEGIN = (
        (1, '8:20'),
        (2, '10:00'),
        (3, '11:40'),
        (4, '13:30'),
        (5, '15:20'),
        (6, '17:00'),
    )

    lecture_begin = models.IntegerField(choices=LECTURE_BEGIN, verbose_name="Начало пары")

    def __str__(self):
        return f"Группа: {self.group} День: {self.day_of_the_week} Пара: {self.lecture_begin}"

    class Meta:
        verbose_name = "Расписание"
        verbose_name_plural = "Расписание"
