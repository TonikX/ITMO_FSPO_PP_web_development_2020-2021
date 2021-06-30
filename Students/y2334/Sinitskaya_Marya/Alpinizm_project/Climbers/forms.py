from django import forms
from django.contrib.admin.widgets import AdminDateWidget

from Climbers.models import *

class ClubForm(forms.Form):
    club_name = forms.CharField(required=True, label = 'Название')
    club_name.widget.attrs.update({'class': 'form-control'})
    club_city = forms.CharField(required=True, label = 'Город')
    club_city.widget.attrs.update({'class': 'form-control'})
    club_mail = forms.EmailField(required=True, label = 'Эл. почта')
    club_mail.widget.attrs.update({'class': 'form-control'})
    club_phone = forms.CharField(required=True, label = 'Телефон')
    club_phone.widget.attrs.update({'class': 'form-control'})
    country = forms.CharField(required=True, label = 'Страна')
    country.widget.attrs.update({'class': 'form-control'})
    club_contact_person = forms.CharField(required=True, label = 'Контакт')
    club_contact_person.widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Club
        fields = ('club_name', 'club_city', 'club_mail', 'club_phone', 'country', 'club_contact_person')


class ClimberForm(forms.Form):
    climber_name = forms.CharField(required=True, label = 'Имя')
    climber_name.widget.attrs.update({'class': 'form-control'})
    climber_surname = forms.CharField(required=True, label = 'Фамилия')
    climber_surname.widget.attrs.update({'class': 'form-control'})
    climber_age = forms.IntegerField(required=True, label = 'Возраст')
    climber_age.widget.attrs.update({'class': 'form-control'})
    climber_xp = forms.IntegerField(required=True, label = 'Опыт')
    climber_xp.widget.attrs.update({'class': 'form-control'})
    climber_address = forms.CharField(required=True, label = 'Адрес')
    climber_address.widget.attrs.update({'class': 'form-control'})
    club = forms.ModelChoiceField(queryset=Club.objects.all(), label = 'Клуб')
    club.widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Climber
        fields = ('climber_name', 'climber_surname', 'climber_age', 'climber_xp', 'climber_address', 'club')


class WaypointForm(forms.Form):
    waypoint_name = forms.CharField(required=True, label='Название')
    waypoint_name.widget.attrs.update({'class': 'form-control'})
    waypoint_desc = forms.CharField(required=True, label='Описание')
    waypoint_desc.widget.attrs.update({'class': 'form-control'})
    mountain = forms.ModelChoiceField(queryset=Mountain.objects.all(), label='Гора')
    mountain.widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Waypoint
        fields = ('waypoint_name', 'waypoint_desc', 'mountain')


class MountainForm(forms.Form):
    mountain_name = forms.CharField(required=True, label='Название')
    mountain_name.widget.attrs.update({'class': 'form-control'})
    mountain_high = forms.CharField(required=True, label='Высота')
    mountain_high.widget.attrs.update({'class': 'form-control'})
    country = forms.CharField(required=True, label='Страна')
    country.widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Mountain
        fields = ('mountain_name', 'mountain_high', 'country')


class GroupForm(forms.Form):
    group_name = forms.CharField(required=True, label='Название')
    group_name.widget.attrs.update({'class': 'form-control'})
    climber = forms.ModelMultipleChoiceField(queryset=Climber.objects.all(), label='Участники')
    climber.widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Group
        fields = ('group_name', 'climber')


class ClimbingForm(forms.Form):
    climbing_start = forms.DateField(required=True, label='Дата старта', widget=AdminDateWidget)
    climbing_start.widget.attrs.update({'class': 'form-control'})
    climbing_finish = forms.DateField(required=True, label='Дата финиша', widget=AdminDateWidget)
    climbing_finish.widget.attrs.update({'class': 'form-control'})
    waypoint = forms.ModelChoiceField(queryset=Waypoint.objects.all(), label='Вершина')
    waypoint.widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Group
        fields = ('climbing_start', 'climbing_finish', 'waypoint')


class AddMembersForm(forms.Form):
    climber = forms.ModelMultipleChoiceField(queryset=Climber.objects.all(), label='Участники')
    climber.widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Group
        fields = ('climber')


class EmergencyForm(forms.Form):
    desc = forms.CharField(required=True, label='Описание', widget=forms.Textarea)
    desc.widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = EmergencySituation
        fields = ('desc', )