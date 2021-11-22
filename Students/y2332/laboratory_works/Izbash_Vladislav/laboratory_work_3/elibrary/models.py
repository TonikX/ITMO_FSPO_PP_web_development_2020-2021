# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Author(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField()

    class Meta:
        managed = False
        db_table = 'Author'


class Book(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField()
    author = models.ForeignKey(Author, models.CASCADE, db_column='author')
    volume = models.IntegerField(null=True)
    orig_lang = models.CharField(max_length=2)
    kind = models.CharField(max_length=10)
    discipline = models.TextField(null=True)
    translator = models.ForeignKey('Translator', models.CASCADE, db_column='translator', null=True)

    class Meta:
        managed = False
        db_table = 'Book'


class BookCopy(models.Model):
    id = models.IntegerField(primary_key=True)
    book_rev = models.ForeignKey('BookRevision', models.CASCADE, db_column='book_rev')
    inv_number = models.CharField(unique=True, max_length=8)
    storage_room = models.IntegerField()
    storage_rack = models.IntegerField()
    storage_shelf = models.IntegerField()
    price = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'BookCopy'


class BookRevision(models.Model):
    id = models.IntegerField(primary_key=True)
    book = models.ForeignKey(Book, models.CASCADE, db_column='book')
    publish_place = models.TextField()
    publish_year = models.IntegerField()
    code = models.TextField(unique=True)
    compilers = models.ManyToManyField('Compiler', through='RevisionCompiler')

    class Meta:
        managed = False
        db_table = 'BookRevision'


class Borrow(models.Model):
    id = models.IntegerField(primary_key=True)
    book_copy = models.ForeignKey('BookCopy', models.DO_NOTHING, db_column='book_copy')
    borrower = models.ForeignKey('Borrower', models.DO_NOTHING, db_column='borrower')
    withdrawal_date = models.DateField()
    return_date = models.DateField()
    returned = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'Borrow'


class Borrower(models.Model):
    id = models.IntegerField(primary_key=True)
    firstname = models.TextField()
    lastname = models.TextField()
    patronymic = models.TextField()
    birthdate = models.DateField()
    address = models.TextField()
    telnumber = models.CharField(max_length=12)
    card_num = models.CharField(unique=True, max_length=8)

    class Meta:
        managed = False
        db_table = 'Borrower'


class Compiler(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField()
    publisher = models.ForeignKey('Publisher', models.DO_NOTHING, db_column='publisher')

    class Meta:
        managed = False
        db_table = 'Compiler'


class Publisher(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField()

    class Meta:
        managed = False
        db_table = 'Publisher'


class RevisionCompiler(models.Model):
    book_rev = models.OneToOneField(BookRevision, models.CASCADE, db_column='book_rev', primary_key=True)
    compiler = models.ForeignKey(Compiler, models.CASCADE, db_column='compiler')

    class Meta:
        managed = False
        db_table = 'RevisionCompiler'
        unique_together = (('book_rev', 'compiler'),)


class Translator(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField()

    class Meta:
        managed = False
        db_table = 'Translator'
