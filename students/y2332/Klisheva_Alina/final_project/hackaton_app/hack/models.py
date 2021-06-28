from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    phoneNumber = models.CharField(max_length=11)
    ROLES = [
        ('0', 'Администратор'),
        ('1', 'Капитан'),
        ('2', 'Жюри')
    ]
    role = models.CharField(choices=ROLES, max_length=1)
    email = models.EmailField(unique=True)
    username = models.CharField(blank=True, max_length=150)
    REQUIRED_FIELDS = ['username', 'role']
    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email


class Issue(models.Model):
    name = models.CharField(max_length=75)
    condition = models.CharField(max_length=5000)
    dateCreate = models.DateField()
    limits = models.CharField(max_length=550, default="нет")
    links = models.CharField(max_length=450, blank=True)
    consultation = models.CharField(max_length=75, blank=True)

    def __str__(self):
        return "Условие задачи: {}; ограничения: {}; доп. материалы: {}; ссылка на консультацию: {}; дата создания:{}".format(
            self.consultation, self.limits, self.links, self.consultation, self.dateCreate)


class Team(models.Model):
    teamName = models.CharField(max_length=100)
    motto = models.CharField(max_length=350)
    captain = models.OneToOneField(User, on_delete=models.CASCADE, related_name='team')
    issue = models.ManyToManyField(Issue, through='Solution', related_name='issue_solution')

    def __str__(self):
        return "Название команды: {}; девиз: {}; капитан: {}; задача: {}".format(self.teamName, self.motto,
                                                                                 self.captain, self.issue)


class Solution(models.Model):
    pubDate = models.DateField()
    score = models.FloatField(max_length=2, null=True)
    comment = models.CharField(max_length=250, null=True)
    solutionLink = models.CharField(max_length=250, default="None")
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='solutions')
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE, related_name='solutions')
    jury = models.ForeignKey(User, on_delete=models.CASCADE, related_name='solutions', default='None', null=True)
    checkDate = models.DateField(null=True, blank=True)

    def __str__(self):
        return "Дата публикации: {}; оценка жюри: {}; комментарий: {}; жюри:{}".format(self.pubDate, self.score,
                                                                                       self.comment, self.jury)


class TeamMember(models.Model):
    ROLES = [
        ('1', 'Developer'),
        ('2', 'Designer'),
        ('3', 'Entrepreneur')
    ]
    fio = models.CharField(max_length=100)
    phoneNumber = models.CharField(max_length=11)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='team_members')
    role = models.CharField(choices=ROLES, max_length=1)

    def __str__(self):
        return "ФИО: {}; тел.: {}; команда: {}; роль: {}".format(self.fio, self.phoneNumber, self.team, self.role)
