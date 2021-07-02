from django.db import models

# Create your models here.


# Модель Почтового отделения
class PostOffice(models.Model):
    id_post_office = models.AutoField(primary_key=True, unique=True)
    number_office = models.IntegerField(verbose_name="Номер отделения", unique=True)
    address_office = models.CharField(max_length=75, verbose_name="Адрес отделения")


# Модель Редакции
class EditorialOffice(models.Model):
    id_editorial_office = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=75, verbose_name="Имя редактора")


# Модель Газеты
class Newspaper(models.Model):
    id_newspaper = models.AutoField(primary_key=True, unique=True)
    title_newspaper = models.CharField(max_length=75, verbose_name="Название газеты")
    cost_newspaper = models.IntegerField(verbose_name="Цена экземпляра")
    publication_index = models.IntegerField(verbose_name="Индекс издания", null=True)
    number_office = models.IntegerField(verbose_name="Номер отделения", null=True)
    date_of_issue = models.DateField(verbose_name="Дата выпуска", null=True)
    id_post_office_fk = models.ForeignKey(PostOffice, on_delete=models.CASCADE, verbose_name="Почтовое отделение (FK)")


# Модель Типографии
class PrintingOffice(models.Model):
    id_printing_office = models.AutoField(primary_key=True, unique=True)
    name_printing_office = models.CharField(max_length=75, verbose_name="Название типографии")
    address_printing_office = models.CharField(max_length=75, verbose_name="Адрес типографии", null=True)
    count = models.IntegerField(verbose_name="Тираж", null=True)
    schedule_printing_office = models.CharField(max_length=75, verbose_name="График работы", null=True)
    id_newspaper_fk = models.ManyToManyField(Newspaper, verbose_name="Газета (FK)")
    post_office = models.ManyToManyField(PostOffice, through="NewspaperDistribution")


# Модель Выпуска
class Release(models.Model):
    id_release = models.AutoField(primary_key=True, unique=True)
    date_of_issue_release = models.DateField(verbose_name="Дата выпуска")
    publication_index_release = models.IntegerField(verbose_name="Индекс издания", null=True)
    cost_copy = models.IntegerField(verbose_name="Цена экземпляра", null=True)
    id_newspaper_fk = models.ForeignKey(Newspaper, on_delete=models.CASCADE, verbose_name="Газета (FK)")
    id_printing_office_fk = models.ForeignKey(PrintingOffice, on_delete=models.CASCADE, verbose_name="Типография (FK)")


# Модель Статьи
class Article(models.Model):
    id_article = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=50, verbose_name="Название статьи")
    id_release_fk = models.ForeignKey(Release, on_delete=models.CASCADE, verbose_name="Выпуск (FK)")


# Модель Правки
class Correction(models.Model):
    id_correction = models.AutoField(primary_key=True, unique=True)
    content = models.CharField(max_length=150, verbose_name="Содержание правки", null=True)
    id_editorial_office_fk = models.ForeignKey(EditorialOffice, on_delete=models.CASCADE, verbose_name="Редакция (FK)")
    id_article_fk = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name="Статья (FK)")


# Модель Распределение газет
class NewspaperDistribution(models.Model):
    id_newspaper_distribution = models.AutoField(primary_key=True, unique=True)
    number_of_copies = models.IntegerField(verbose_name="Цена экземпляра", null=True)
    cost_release = models.IntegerField(verbose_name="Цена экземпляра", null=True)
    id_printing_office_fk = models.ForeignKey(PrintingOffice, on_delete=models.CASCADE, verbose_name="Типография (FK)")
    id_post_office_fk = models.ForeignKey(PostOffice, on_delete=models.CASCADE, verbose_name="Почтовое отделение (FK)")
