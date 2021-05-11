from django import forms
from django.contrib.auth.models import User

from labor.settings import AUTH_USER_MODEL
from labor_app.models import Jobless, EducationalOrganization, Stipend, EducationalGroup, Passage, EducationalProgram


class JoblessForm(forms.ModelForm):
    username=forms.CharField(max_length=50,required=True)
    password=forms.CharField(max_length=50,widget=forms.PasswordInput)
    address=forms.CharField(max_length=500,required=False)
    lfm=forms.CharField(max_length=200,required=True)
    tel=forms.CharField(max_length=13,required=True)
    passport=forms.CharField(max_length=15,required=True)
    workexp=forms.IntegerField(required=True)
    email=forms.EmailField(max_length=50,widget=forms.EmailInput,required=False)

    class Meta:
        model=Jobless
        fields=(
            'username',
            'password',
            'address',
            'lfm',
            'tel',
            'passport',
            'workexp',
            'email',
        )
class JoblessEditForm(forms.ModelForm):
    username=forms.CharField(max_length=50,required=True)
    address=forms.CharField(max_length=500,required=False)
    lfm=forms.CharField(max_length=200,required=True)
    tel=forms.CharField(max_length=13,required=True)
    passport=forms.CharField(max_length=15,required=True)
    workexp=forms.IntegerField(required=True)
    email=forms.EmailField(max_length=50,widget=forms.EmailInput,required=False)
    organization=forms.ModelChoiceField(queryset=EducationalOrganization.objects.all(),required=False)

    class Meta:
        model=Jobless
        fields=(
            'username',
            'address',
            'lfm',
            'tel',
            'passport',
            'workexp',
            'email',
            'organization',
        )


class OrganizationForm(forms.ModelForm):
    TYPE_EN = [('SPO', 'СПО'),
               ('SOO', 'СОО'),
               ('HS', 'ВО'),
               ('SO', 'СО')
    ]
    name = forms.CharField(max_length=200)
    type = forms.ChoiceField(choices=TYPE_EN)
    address = forms.CharField(max_length=500)
    class Meta:
        model=EducationalOrganization
        fields=(
            'name',
            'type',
            'address',
        )

class StipendForm(forms.ModelForm):
    jobless = forms.ModelChoiceField(queryset=Jobless.objects.all())
    value=forms.IntegerField()
    startprov=forms.DateTimeField()
    finprov=forms.DateTimeField()
    class Meta:
        model=Stipend
        fields=(
            'jobless',
            'value',
            'startprov',
            'finprov',
        )

class GroupForm(forms.ModelForm):
    program=forms.ModelChoiceField(queryset=EducationalProgram.objects.all())
    maxquanstud=forms.IntegerField()
    class Meta:
        model=EducationalGroup
        fields=(
            'program',
            'maxquanstud',
        )

class PassageForm(forms.ModelForm):
    jobless=forms.ModelChoiceField(queryset=Jobless.objects.all())
    group=forms.ModelChoiceField(queryset=EducationalGroup.objects.all())
    statofadopt=forms.NullBooleanField()
    document=forms.NullBooleanField()
    class Meta:
        model=Passage
        fields=(
            'jobless',
            'group',
            'statofadopt',
            'document',
        )

class ProgramForm(forms.ModelForm):
    name=forms.CharField(max_length=200)
    startdate = forms.DateField()
    finishdate = forms.DateField()
    cost= forms.IntegerField()
    type=forms.CharField(max_length=20)
    description=forms.CharField(max_length=500,required=False)
    class Meta:
        model=EducationalProgram
        fields=(
            'name',
            'startdate',
            'finishdate',
            'cost',
            'type',
            'description'
        )
