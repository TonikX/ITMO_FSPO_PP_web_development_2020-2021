import time
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

def generate_imageset_upload_to(instance, filename=None):
    return f'images/{instance.id}_{str(int(time.time()))}.png'

class Profile(models.Model):
    ADMIN = 'ADM'
    CLIENT = 'CLI'
    USER_PERMISSION_CHOICES = [
        (ADMIN, 'Админ'),
        (CLIENT, 'Пользователь'),
    ]
    role = models.CharField(
        max_length=3,
        choices=USER_PERMISSION_CHOICES,
        default=CLIENT
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.TextField(max_length=12, blank=True)
    image = models.ImageField(blank=True, null=True, upload_to=generate_imageset_upload_to)

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

    def __str__(self):
        return self.user.username 

class Articles(models.Model):
    HISTORY = 'HIS'
    LITER = 'LIT'
    ARTICLE_PERMISSION_CHOICES = [
        (HISTORY, 'Историческая'),
        (LITER, 'Литературная'),
    ]
    type = models.CharField(
        max_length=3,
        choices=ARTICLE_PERMISSION_CHOICES,
        verbose_name="Тип"
    )
    article_title = models.TextField(verbose_name="Название")
    discription = models.TextField(verbose_name="Описание")
    content = models.TextField(verbose_name="Содержимое")
    status = models.BooleanField(default=False, verbose_name="Статус")
    image = models.ImageField(blank=True, null=True, upload_to=generate_imageset_upload_to)

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Создатель")


    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"

    def __str__(self):
        return self.article_title

class Writer(models.Model):
    name = models.TextField(verbose_name="Имя")
    date_life = models.TextField(verbose_name="Даты жизни")
    biografi = models.TextField(verbose_name="Биография")
    bibliografi = models.TextField(verbose_name="Библиография")
    about_life = models.TextField(verbose_name="Произведения о жизни")
    status = models.BooleanField(default=False, verbose_name="Статус")
    image = models.ImageField(blank=True, null=True, upload_to=generate_imageset_upload_to)


    class Meta:
        verbose_name = "Писатель"
        verbose_name_plural = "Писатели"

    def __str__(self):
        return self.name

class Books(models.Model):
    BOOK = 'DEF'
    PROSE = 'PRS'
    BOOK_PERMISSION_CHOICES = [
        (BOOK, 'Книги'),
        (PROSE, 'Проза'),
    ]
    type = models.CharField(
        max_length=3,
        choices=BOOK_PERMISSION_CHOICES,
        verbose_name="Тип"
    )
    author = models.ForeignKey(Writer, on_delete=models.CASCADE, verbose_name="Создатель")
    title = models.TextField(verbose_name="Название")
    date = models.TextField(blank=True, null=True, verbose_name="Дата написания")
    discription = models.TextField(verbose_name="Описание")
    anatation = models.TextField(verbose_name="Аннотация")
    text = models.TextField(blank=True, null=True, verbose_name="Текст")
    plus_rating = models.IntegerField( verbose_name="Положительный рейтинг")
    words = models.IntegerField(blank=True, null=True, verbose_name="Количество слов")
    chapters = models.IntegerField(blank=True, null=True, verbose_name="Количество глав")
    minus_rating = models.IntegerField( verbose_name="Отрицательный рейтинг")
    status = models.BooleanField(default=False, verbose_name="Статус")
    image = models.ImageField(blank=True, null=True, upload_to=generate_imageset_upload_to)

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Создатель")


    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"

    def __str__(self):
        return self.title

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Создатель")
    book = models.ForeignKey(Books, on_delete=models.CASCADE, verbose_name="Книга")
    title = models.TextField(verbose_name="Название")
    discription = models.TextField(verbose_name="Описание")
    minus_rating = models.IntegerField( verbose_name="Отрицательный рейтинг")
    plus_rating = models.IntegerField( verbose_name="Положительный рейтинг")

    class Meta:
        verbose_name = "Рецензия"
        verbose_name_plural = "Рецензии"

    def __str__(self):
        return self.title

class Discussion(models.Model):
    title = models.TextField(verbose_name="Название")
    book = models.ForeignKey(Books, on_delete=models.CASCADE, verbose_name="Книга")

    class Meta:
        verbose_name = "Дискуссия"
        verbose_name_plural = "Дискуссии"

    def __str__(self):
        return self.title

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Создатель")
    discussion = models.ForeignKey(Discussion, on_delete=models.CASCADE, verbose_name="Тема дискуссии")
    text = models.TextField(blank=True, null=True, verbose_name="Текст")

    class Meta:
        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщения"

    def __str__(self):
        return self.text

class Likes(models.Model):
    LIK = 'LIK'
    DIS = 'DIS'
    LIKES_PERMISSION_CHOICES = [
        (LIK, 'Лайк'),
        (DIS, 'Дислайк'),
    ]
    type = models.CharField(
        max_length=3,
        choices=LIKES_PERMISSION_CHOICES,
        verbose_name="Тип"
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Создатель")
    book = models.ForeignKey(Books, on_delete=models.CASCADE, verbose_name="Книга")

    class Meta:
        verbose_name = "Лайк"
        verbose_name_plural = "Лайки"

    def __str__(self):
        return self.type

class LikesReview(models.Model):
    LIK = 'LIK'
    DIS = 'DIS'
    LIKES_PERMISSION_CHOICES = [
        (LIK, 'Лайк'),
        (DIS, 'Дислайк'),
    ]
    type = models.CharField(
        max_length=3,
        choices=LIKES_PERMISSION_CHOICES,
        verbose_name="Тип"
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Создатель")
    review = models.ForeignKey(Review, on_delete=models.CASCADE, verbose_name="Статья")

    class Meta:
        verbose_name = "Лайк рецензии"
        verbose_name_plural = "Лайки рецинзий"

    def __str__(self):
        return self.type


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
