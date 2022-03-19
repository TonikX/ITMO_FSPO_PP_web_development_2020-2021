from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _
from django.db import models


def gte_zero(value):
    if value < 0:
        raise ValidationError(
            _('Should be greater than or equal to zero'),
            params={'value': value},
        )


def gt_zero(value):
    if value < 1:
        raise ValidationError(
            _('Should be greater than zero'),
            params={'value': value},
        )


class Direction(models.Model):
    code = models.CharField(
        max_length=8,
        verbose_name="Код",
        validators=[
            RegexValidator(
                regex=r"^\d{2}\.\d{2}\.\d{2}$",
                message="Wrong format"
            )
        ]
    )
    name = models.CharField(max_length=100, verbose_name="Название")

    def __str__(self):
        return self.code

    class Meta:
        verbose_name = "Направление"
        verbose_name_plural = "Направления"


class Syllabus(models.Model):
    year = models.CharField(
        max_length=9,
        verbose_name="Год",
        validators=[
            RegexValidator(
                regex=r"^\d{4}/\d{4}$",
                message="Wrong format"
            )
        ]
    )
    specialty_code = models.CharField(max_length=100, verbose_name="Код специальности")
    specialty_name = models.CharField(max_length=100, verbose_name="Название специальности")
    direction = models.ForeignKey(Direction, on_delete=models.CASCADE, verbose_name="Направление")

    def __str__(self):
        return f"{self.year} {self.specialty_name}"

    class Meta:
        verbose_name = "Учебный план"
        verbose_name_plural = "Учебные планы"


class Discipline(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    code = models.CharField(max_length=100, verbose_name="Код")
    syllabus = models.ForeignKey(Syllabus, on_delete=models.CASCADE, verbose_name="Учебный план")
    cycle = models.CharField(max_length=100, verbose_name="Цикл")

    hours_total = models.SmallIntegerField(verbose_name="Всего часов", validators=[gte_zero])
    hours_lec = models.SmallIntegerField(verbose_name="Лек.", validators=[gte_zero], null=True, blank=True)
    hours_pr = models.SmallIntegerField(verbose_name="Прак.", validators=[gte_zero], null=True, blank=True)
    hours_la = models.SmallIntegerField(verbose_name="Лаб.", validators=[gte_zero], null=True, blank=True)
    hours_isw = models.SmallIntegerField(verbose_name="СРС", validators=[gte_zero], null=True, blank=True)
    hours_cons = models.SmallIntegerField(verbose_name="Конс.", validators=[gte_zero], null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Дисциплина"
        verbose_name_plural = "Дисциплины"


class Lecturer(models.Model):
    first_name = models.CharField(max_length=30, verbose_name="Имя")
    surname = models.CharField(max_length=30, verbose_name="Фамилия")
    patronymic = models.CharField(max_length=30, null=True, blank=True, verbose_name="Отчество")
    disciplines = models.ManyToManyField(Discipline, verbose_name="Дисциплины")

    def __str__(self):
        return f"{self.surname} {self.first_name} {self.patronymic or ''}"

    class Meta:
        verbose_name = "Преподаватель"
        verbose_name_plural = "Преподаватели"


class Group(models.Model):
    number = models.CharField(max_length=5, verbose_name="Номер")
    students_count = models.IntegerField(verbose_name="Количество студентов", validators=[gte_zero])
    syllabus = models.ForeignKey(Syllabus, on_delete=models.CASCADE, verbose_name="Учебный план")

    def __str__(self):
        return self.number

    class Meta:
        verbose_name = "Группа"
        verbose_name_plural = "Группы"


class Classroom(models.Model):
    number = models.CharField(
        max_length=3,
        verbose_name="Номер",
        unique=True,
        validators=[
            RegexValidator(
                regex=r"^\d{3}$",
                message="Wrong format"
            )
        ]
    )
    type = models.CharField(max_length=30, null=True, blank=True, verbose_name="Тип аудитории")
    seats_count = models.SmallIntegerField(verbose_name="Количество мест", validators=[gte_zero])

    def __str__(self):
        return self.number

    class Meta:
        verbose_name = "Аудитория"
        verbose_name_plural = "Аудитории"


DAYS_OF_WEEK = (
    (1, 'Понедельник'),
    (2, 'Вторник'),
    (3, 'Среда'),
    (4, 'Четверг'),
    (5, 'Пятница'),
    (6, 'Суббота'),
)

LECTURE_BEGIN = (
    (1, '8:20'),
    (2, '10:00'),
    (3, '11:40'),
    (4, '13:30'),
    (5, '15:20'),
    (6, '17:00'),
)

LECTURE_TYPE = (
    (1, 'Лек.'),
    (2, 'Лаб.'),
    (3, 'Прак.'),
    (4, 'СРС'),
)


class Schedule(models.Model):
    lecturer = models.ForeignKey(Lecturer, on_delete=models.CASCADE, verbose_name="Преподаватель")
    discipline = models.ForeignKey(Discipline, on_delete=models.CASCADE, verbose_name="Дисциплина")
    group = models.ForeignKey(Group, on_delete=models.CASCADE, verbose_name="Группа")
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE, verbose_name="Аудитория")
    lecture_type = models.SmallIntegerField(choices=LECTURE_TYPE, verbose_name="Тип занятия")

    semester = models.SmallIntegerField(verbose_name="Семестр", validators=[gt_zero])
    week_parity = models.BooleanField(verbose_name="Неделя чёт/нечёт")
    day_of_the_week = models.SmallIntegerField(choices=DAYS_OF_WEEK, verbose_name="День недели")
    lecture_begin = models.SmallIntegerField(choices=LECTURE_BEGIN, verbose_name="Начало пары")

    def __str__(self):
        return f"Семестр: {self.semester} Группа: {self.group} День: {self.day_of_the_week} Пара: {self.lecture_begin}"

    class Meta:
        verbose_name = "Расписание"
        verbose_name_plural = "Расписание"
