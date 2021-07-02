from django import forms

from .models import *


class PostOfficeForm(forms.Form):
    number_office = forms.IntegerField(required=True, label='Номер почты')
    number_office.widget.attrs.update({'class': 'form-control'})
    address_office = forms.CharField(max_length=75, required=True, label='Адрес почты')
    address_office.widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = PostOffice
        fields = ('number_office', 'address_office')


class EditorialOfficeForm(forms.Form):
    name = forms.CharField(max_length=75, required=True, label='Имя редактора')
    name.widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = EditorialOffice
        fields = ('name')


class NewspaperForm(forms.Form):
    title_newspaper = forms.CharField(max_length=75, required=True, label="Название газеты")
    title_newspaper.widget.attrs.update({'class': 'form-control'})
    cost_newspaper = forms.IntegerField(required=True, label="Цена экземпляра")
    cost_newspaper.widget.attrs.update({'class': 'form-control'})
    publication_index = forms.IntegerField(required=False, label="Индекс издания")
    publication_index.widget.attrs.update({'class': 'form-control'})
    number_office = forms.IntegerField(required=False, label="Номер отделения")
    number_office.widget.attrs.update({'class': 'form-control'})
    date_of_issue = forms.DateField(required=False, label="Дата выпуска")
    date_of_issue.widget.attrs.update({'class': 'form-control'})
    id_post_office_fk = forms.ModelChoiceField(queryset=PostOffice.objects.all(), label='Почтовое отделение (FK)')
    id_post_office_fk.widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Newspaper
        fields = ('title_newspaper', 'cost_newspaper', 'publication_index', 'number_office', 'date_of_issue', 'id_post_office_fk')


class PrintingOfficeForm(forms.Form):
    name_printing_office = forms.CharField(max_length=75, required=True, label="Название типографии")
    name_printing_office.widget.attrs.update({'class': 'form-control'})
    address_printing_office = forms.CharField(required=False, label="Адрес типографии")
    address_printing_office.widget.attrs.update({'class': 'form-control'})
    count = forms.IntegerField(required=False, label="Тираж")
    count.widget.attrs.update({'class': 'form-control'})
    schedule_printing_office = forms.CharField(max_length=75, required=False, label="График работы")
    schedule_printing_office.widget.attrs.update({'class': 'form-control'})
    id_newspaper_fk = forms.ModelMultipleChoiceField(queryset=Newspaper.objects.all(), label='Газета (FK)')
    id_newspaper_fk.widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = PrintingOffice
        fields = ('name_printing_office', 'address_printing_office', 'count', 'schedule_printing_office', 'id_newspaper_fk')


class ReleaseForm(forms.Form):
    date_of_issue_release = forms.DateField(label="Дата выпуска")
    date_of_issue_release.widget.attrs.update({'class': 'form-control'})
    publication_index_release = forms.IntegerField(required=False, label="Индекс издания")
    publication_index_release.widget.attrs.update({'class': 'form-control'})
    cost_copy = forms.IntegerField(required=False, label="Цена экземпляра")
    cost_copy.widget.attrs.update({'class': 'form-control'})
    id_newspaper_fk = forms.ModelChoiceField(queryset=Newspaper.objects.all(), label='Газета (FK)')
    id_newspaper_fk.widget.attrs.update({'class': 'form-control'})
    id_printing_office_fk = forms.ModelChoiceField(queryset=PrintingOffice.objects.all(), label='Типография (FK)')
    id_printing_office_fk.widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Release
        fields = ('date_of_issue_release', 'publication_index_release', 'cost_copy', 'id_newspaper_fk', 'id_printing_office_fk')



class ArticleForm(forms.Form):
    name = forms.CharField(max_length=50, required=True, label="Название статьи")
    name.widget.attrs.update({'class': 'form-control'})
    id_release_fk = forms.ModelChoiceField(queryset=Release.objects.all(), label='Выпуск (FK)')
    id_release_fk.widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Article
        fields = ('name', 'id_release_fk')


class CorrectionForm(forms.Form):
    content = forms.CharField(max_length=150, required=True, label="Содержание правки")
    content.widget.attrs.update({'class': 'form-control'})
    id_editorial_office_fk = forms.ModelChoiceField(queryset=EditorialOffice.objects.all(), label='Редакция (FK)')
    id_editorial_office_fk.widget.attrs.update({'class': 'form-control'})
    id_article_fk = forms.ModelChoiceField(queryset=Article.objects.all(), label='Статья (FK)')
    id_article_fk.widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Article
        fields = ('content', 'id_editorial_office_fk', 'id_article_fk')


class NewspaperDistributionForm(forms.Form):
    number_of_copies = forms.IntegerField(required=False, label="Количество экземляров")
    number_of_copies.widget.attrs.update({'class': 'form-control'})
    cost_release = forms.IntegerField(required=False, label="Цена экземпляра")
    cost_release.widget.attrs.update({'class': 'form-control'})
    id_printing_office_fk = forms.ModelChoiceField(queryset=PrintingOffice.objects.all(), label='Типография (FK)')
    id_printing_office_fk.widget.attrs.update({'class': 'form-control'})
    id_post_office_fk = forms.ModelChoiceField(queryset=PostOffice.objects.all(), label='Почтовое отделение (FK)')
    id_post_office_fk.widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = NewspaperDistribution
        fields = ('number_of_copies', 'cost_release', 'id_printing_office_fk', 'id_post_office_fk')
