from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .forms import *
from .models import *
from django.views import View
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views.generic.edit import UpdateView

# Create your views here.


def getMain(request):
    return render(request, 'main.html')


class ViewAllPostOffices(View):

    def get(self, request):
        postoffices = PostOffice.objects.all()
        return render(request, "PostOffice/PostOfficeView.html", context={"postoffices": postoffices})


class AddPostOffices(View):

    def get(self, request):
        form = PostOfficeForm()
        return render(request, "PostOffice/PostOfficeCreate.html", context={"form": form})

    def post(self, request):
        form = PostOfficeForm(request.POST)
        if form.is_valid():
            PostOffice.objects.create(number_office=form.cleaned_data["number_office"],
                                      address_office=form.cleaned_data["address_office"])
        return HttpResponseRedirect('/PostOffice/PostOfficeView')


class EditPostOffices(View):

    def get(self, request, id_post_office):
        post_office = get_object_or_404(PostOffice, id_post_office=id_post_office)
        form = PostOfficeForm(initial={
            'number_office': post_office.number_office,
            'address_office': post_office.address_office,
        })
        return render(request, "PostOffice/PostOfficeEdit.html", context={"form": form, "post_office": post_office})

    def post(self, request, id_post_office):
        form = PostOfficeForm(request.POST)
        if form.is_valid():
            PostOffice.objects.filter(id_post_office=id_post_office).update(
                number_office=form.cleaned_data["number_office"],
                address_office=form.cleaned_data["address_office"])
            return HttpResponseRedirect("/PostOffice/PostOfficeView/")
        redirect = '/PostOfficeEdit/{}'.format(id_post_office)
        return HttpResponseRedirect(redirect)


class DeletePostOffices(View):

    def get(self, request, id_post_office):
        post_office = get_object_or_404(PostOffice, id_post_office=id_post_office)
        post_office.delete()
        return HttpResponseRedirect('/PostOffice/PostOfficeView/')




class ViewAllEditorialOffices(View):

    def get(self, request):
        editorialoffices = EditorialOffice.objects.all()
        return render(request, "EditorialOffice/EditorialOfficeView.html", context={"editorialoffices": editorialoffices})


class AddEditorialOffices(View):

    def get(self, request):
        form = EditorialOfficeForm()
        return render(request, "EditorialOffice/EditorialOfficeCreate.html", context={"form": form})

    def post(self, request):
        form = EditorialOfficeForm(request.POST)
        if form.is_valid():
            EditorialOffice.objects.create(name=form.cleaned_data["name"])
        return HttpResponseRedirect('/EditorialOffice/EditorialOfficeView')


class EditEditorialOffices(View):

    def get(self, request, id_editorial_office):
        editorial_office = get_object_or_404(EditorialOffice, id_editorial_office=id_editorial_office)
        form = EditorialOfficeForm(initial={
            'name': editorial_office.name
        })
        return render(request, "EditorialOffice/EditorialOfficeEdit.html", context={"form": form, "editorial_office": editorial_office})

    def post(self, request, id_editorial_office):
        form = EditorialOfficeForm(request.POST)
        if form.is_valid():
            EditorialOffice.objects.filter(id_editorial_office=id_editorial_office).update(
                name=form.cleaned_data["name"])
            return HttpResponseRedirect("/EditorialOffice/EditorialOfficeView/")
        redirect = '/EditorialOfficeEdit/{}'.format(id_editorial_office)
        return HttpResponseRedirect(redirect)


class DeleteEditorialOffices(View):

    def get(self, request, id_editorial_office):
        editorial_office = get_object_or_404(EditorialOffice, id_editorial_office=id_editorial_office)
        editorial_office.delete()
        return HttpResponseRedirect('/EditorialOffice/EditorialOfficeView/')



class ViewAllNewspapers(View):

    def get(self, request):
        newspapers = Newspaper.objects.all()
        return render(request, "Newspaper/NewspaperView.html", context={"newspapers": newspapers})


class AddNewspapers(View):

    def get(self, request):
        form = NewspaperForm()
        return render(request, "Newspaper/NewspaperCreate.html", context={"form": form})

    def post(self, request):
        form = NewspaperForm(request.POST)
        if form.is_valid():
            Newspaper.objects.create(title_newspaper=form.cleaned_data["title_newspaper"],
                                     cost_newspaper=form.cleaned_data["cost_newspaper"],
                                     publication_index=form.cleaned_data["publication_index"],
                                     number_office=form.cleaned_data["number_office"],
                                     date_of_issue=form.cleaned_data["date_of_issue"],
                                     id_post_office_fk=form.cleaned_data["id_post_office_fk"])
        return HttpResponseRedirect('/Newspaper/NewspaperView')


class EditNewspapers(View):

    def get(self, request, id_newspaper):
        newspaper = get_object_or_404(Newspaper, id_newspaper=id_newspaper)
        form = NewspaperForm(initial={
            'title_newspaper': newspaper.title_newspaper,
            'cost_newspaper': newspaper.cost_newspaper,
            'publication_index': newspaper.publication_index,
            'number_office': newspaper.number_office,
            'date_of_issue': newspaper.date_of_issue,
            'id_post_office_fk': newspaper.id_post_office_fk,
        })
        return render(request, "Newspaper/NewspaperEdit.html", context={"form": form, "newspaper": newspaper})

    def post(self, request, id_newspaper):
        form = NewspaperForm(request.POST)
        if form.is_valid():
            Newspaper.objects.filter(id_newspaper=id_newspaper).update(
                title_newspaper=form.cleaned_data["title_newspaper"],
                cost_newspaper=form.cleaned_data["cost_newspaper"],
                publication_index=form.cleaned_data["publication_index"],
                number_office=form.cleaned_data["number_office"],
                date_of_issue=form.cleaned_data["date_of_issue"],
                id_post_office_fk=form.cleaned_data["id_post_office_fk"])
            return HttpResponseRedirect("/Newspaper/NewspaperView/")
        redirect = '/NewspaperEdit/{}'.format(id_newspaper)
        return HttpResponseRedirect(redirect)


class DeleteNewspapers(View):

    def get(self, request, id_newspaper):
        newspaper = get_object_or_404(Newspaper, id_newspaper=id_newspaper)
        newspaper.delete()
        return HttpResponseRedirect('/Newspaper/NewspaperView/')




class ViewAllPrintingOffices(View):

    def get(self, request):
        printingoffices = PrintingOffice.objects.all()
        return render(request, "PrintingOffice/PrintingOfficeView.html", context={"printingoffices": printingoffices})


class AddPrintingOffices(View):

    def get(self, request):
        form = PrintingOfficeForm()
        return render(request, "PrintingOffice/PrintingOfficeCreate.html", context={"form": form})

    def post(self, request):
        form = PrintingOfficeForm(request.POST)
        if form.is_valid():
            PrintingOffice.objects.create(name_printing_office=form.cleaned_data["name_printing_office"],
                                          address_printing_office=form.cleaned_data["address_printing_office"],
                                          count=form.cleaned_data["count"],
                                          schedule_printing_office=form.cleaned_data["schedule_printing_office"],
                                          id_newspaper_fk=form.cleaned_data["id_newspaper_fk"])
        return HttpResponseRedirect('/PrintingOffice/PrintingOfficeView')


class EditPrintingOffices(View):

    def get(self, request, id_printing_office):
        printingoffice = get_object_or_404(PrintingOffice, id_printing_office=id_printing_office)
        form = PrintingOfficeForm(initial={
            'name_printing_office': printingoffice.name_printing_office,
            'address_printing_office': printingoffice.address_printing_office,
            'count': printingoffice.count,
            'schedule_printing_office': printingoffice.schedule_printing_office,
            'id_newspaper_fk': printingoffice.id_newspaper_fk,
        })
        return render(request, "PrintingOffice/PrintingOfficeEdit.html", context={"form": form, "printingoffice": printingoffice})

    def post(self, request, id_printing_office):
        form = PrintingOfficeForm(request.POST)
        if form.is_valid():
            PrintingOffice.objects.filter(id_printing_office=id_printing_office).update(
                name_printing_office=form.cleaned_data["name_printing_office"],
                address_printing_office=form.cleaned_data["address_printing_office"],
                count=form.cleaned_data["count"],
                schedule_printing_office=form.cleaned_data["schedule_printing_office"],
                id_newspaper_fk=form.cleaned_data["id_newspaper_fk"])
            return HttpResponseRedirect("/PrintingOffice/PrintingOfficeView/")
        redirect = '/PrintingOfficeEdit/{}'.format(id_printing_office)
        return HttpResponseRedirect(redirect)


class DeletePrintingOffices(View):

    def get(self, request, id_printing_office):
        printingoffice = get_object_or_404(PrintingOffice, id_printing_office=id_printing_office)
        printingoffice.delete()
        return HttpResponseRedirect('/PrintingOffice/PrintingOfficeView/')




class ViewAllReleases(View):

    def get(self, request):
        releases = Release.objects.all()
        return render(request, "Release/ReleaseView.html", context={"releases": releases})


class AddReleases(View):

    def get(self, request):
        form = ReleaseForm()
        return render(request, "Release/ReleaseCreate.html", context={"form": form})

    def post(self, request):
        form = ReleaseForm(request.POST)
        if form.is_valid():
            Release.objects.create(date_of_issue_release=form.cleaned_data["date_of_issue_release"],
                                   publication_index_release=form.cleaned_data["publication_index_release"],
                                   cost_copy=form.cleaned_data["cost_copy"],
                                   id_newspaper_fk=form.cleaned_data["id_newspaper_fk"],
                                   id_printing_office_fk=form.cleaned_data["id_printing_office_fk"])
        return HttpResponseRedirect('/Release/ReleaseView')


class EditReleases(View):

    def get(self, request, id_release):
        release = get_object_or_404(Release, id_release=id_release)
        form = ReleaseForm(initial={
            'date_of_issue_release': release.date_of_issue_release,
            'publication_index_release': release.publication_index_release,
            'cost_copy': release.cost_copy,
            'id_newspaper_fk': release.id_newspaper_fk,
            'id_printing_office_fk': release.id_printing_office_fk,
        })
        return render(request, "Release/ReleaseEdit.html", context={"form": form, "release": release})

    def post(self, request, id_release):
        form = ReleaseForm(request.POST)
        if form.is_valid():
            Release.objects.filter(id_release=id_release).update(
                date_of_issue_release=form.cleaned_data["date_of_issue_release"],
                publication_index_release=form.cleaned_data["publication_index_release"],
                cost_copy=form.cleaned_data["cost_copy"],
                id_newspaper_fk=form.cleaned_data["id_newspaper_fk"],
                id_printing_office_fk=form.cleaned_data["id_printing_office_fk"])
            return HttpResponseRedirect("/Release/ReleaseView/")
        redirect = '/ReleaseEdit/{}'.format(id_release)
        return HttpResponseRedirect(redirect)


class DeleteReleases(View):

    def get(self, request, id_release):
        release = get_object_or_404(Release, id_release=id_release)
        release.delete()
        return HttpResponseRedirect('/Release/ReleaseView/')




class ViewAllArticles(View):

    def get(self, request):
        articles = Article.objects.all()
        return render(request, "Article/ArticleView.html", context={"articles": articles})


class AddArticles(View):

    def get(self, request):
        form = ArticleForm()
        return render(request, "Article/ArticleCreate.html", context={"form": form})

    def post(self, request):
        form = ArticleForm(request.POST)
        if form.is_valid():
            Article.objects.create(name=form.cleaned_data["name"],
                                   id_release_fk=form.cleaned_data["id_release_fk"])
        return HttpResponseRedirect('/Article/ArticleView')


class EditArticles(View):

    def get(self, request, id_article):
        article = get_object_or_404(Article, id_article=id_article)
        form = ArticleForm(initial={
            'name': article.name,
            'id_release_fk': article.id_release_fk,
        })
        return render(request, "Article/ArticleEdit.html", context={"form": form, "article": article})

    def post(self, request, id_article):
        form = ArticleForm(request.POST)
        if form.is_valid():
            Article.objects.filter(id_article=id_article).update(
                                   name=form.cleaned_data["name"],
                                   id_release_fk=form.cleaned_data["id_release_fk"])
            return HttpResponseRedirect("/Article/ArticleView/")
        redirect = '/ArticleEdit/{}'.format(id_article)
        return HttpResponseRedirect(redirect)


class DeleteArticles(View):

    def get(self, request, id_article):
        article = get_object_or_404(Article, id_article=id_article)
        article.delete()
        return HttpResponseRedirect('/Article/ArticleView/')




class ViewAllCorrections(View):

    def get(self, request):
        corrections = Correction.objects.all()
        return render(request, "Correction/CorrectionView.html", context={"corrections": corrections})


class AddCorrections(View):

    def get(self, request):
        form = CorrectionForm()
        return render(request, "Correction/CorrectionCreate.html", context={"form": form})

    def post(self, request):
        form = CorrectionForm(request.POST)
        if form.is_valid():
            Correction.objects.create(content=form.cleaned_data["content"],
                                      id_editorial_office_fk=form.cleaned_data["id_editorial_office_fk"],
                                      id_article_fk=form.cleaned_data["id_article_fk"])
        return HttpResponseRedirect('/Correction/CorrectionView')


class EditCorrections(View):

    def get(self, request, id_correction):
        correction = get_object_or_404(Correction, id_correction=id_correction)
        form = CorrectionForm(initial={
                              'content': correction.content,
                              'id_editorial_office_fk': correction.id_editorial_office_fk,
                              'id_article_fk': correction.id_article_fk,
        })
        return render(request, "Correction/CorrectionEdit.html", context={"form": form, "correction": correction})

    def post(self, request, id_correction):
        form = ArticleForm(request.POST)
        if form.is_valid():
            Correction.objects.filter(id_correction=id_correction).update(
                                      content=form.cleaned_data["content"],
                                      id_editorial_office_fk=form.cleaned_data["id_editorial_office_fk"],
                                      id_article_fk=form.cleaned_data["id_article_fk"])
            return HttpResponseRedirect("/Correction/CorrectionView/")
        redirect = '/CorrectionEdit/{}'.format(id_correction)
        return HttpResponseRedirect(redirect)


class DeleteCorrections(View):

    def get(self, request, id_correction):
        correction = get_object_or_404(Correction, id_correction=id_correction)
        correction.delete()
        return HttpResponseRedirect('/Correction/CorrectionView/')




class ViewAllNewspaperDistributions(View):

    def get(self, request):
        newspaperdistributions = NewspaperDistribution.objects.all()
        return render(request, "NewspaperDistribution/NewspaperDistributionView.html", context={"newspaperdistributions": newspaperdistributions})


class AddNewspaperDistributions(View):

    def get(self, request):
        form = NewspaperDistributionForm()
        return render(request, "NewspaperDistribution/NewspaperDistributionCreate.html", context={"form": form})

    def post(self, request):
        form = NewspaperDistributionForm(request.POST)
        if form.is_valid():
            NewspaperDistribution.objects.create(number_of_copies=form.cleaned_data["number_of_copies"],
                                                 cost_release=form.cleaned_data["cost_release"],
                                                 id_printing_office_fk=form.cleaned_data["id_printing_office_fk"],
                                                 id_post_office_fk=form.cleaned_data["id_post_office_fk"])
        return HttpResponseRedirect('/NewspaperDistribution/NewspaperDistributionView')


class EditNewspaperDistributions(View):

    def get(self, request, id_newspaper_distribution):
        newspaperdistribution = get_object_or_404(NewspaperDistribution, id_newspaper_distribution=id_newspaper_distribution)
        form = NewspaperDistributionForm(initial={
                                         'number_of_copies': newspaperdistribution.number_of_copies,
                                         'cost_release': newspaperdistribution.cost_release,
                                         'id_printing_office_fk': newspaperdistribution.id_printing_office_fk,
                                         'id_post_office_fk': newspaperdistribution.id_post_office_fk,
        })
        return render(request, "NewspaperDistribution/NewspaperDistributionEdit.html", context={"form": form, "newspaperdistribution": newspaperdistribution})

    def post(self, request, id_newspaper_distribution):
        form = NewspaperDistributionForm(request.POST)
        if form.is_valid():
            NewspaperDistribution.objects.filter(id_newspaper_distribution=id_newspaper_distribution).update(
                                                 number_of_copies=form.cleaned_data["number_of_copies"],
                                                 cost_release=form.cleaned_data["cost_release"],
                                                 id_printing_office_fk=form.cleaned_data["id_printing_office_fk"],
                                                 id_post_office_fk=form.cleaned_data["id_post_office_fk"])
            return HttpResponseRedirect("/NewspaperDistribution/NewspaperDistributionView/")
        redirect = '/NewspaperDistributionEdit/{}'.format(id_newspaper_distribution)
        return HttpResponseRedirect(redirect)


class DeleteNewspaperDistributions(View):

    def get(self, request, id_newspaper_distribution):
        newspaperdistribution = get_object_or_404(NewspaperDistribution, id_newspaper_distribution=id_newspaper_distribution)
        newspaperdistribution.delete()
        return HttpResponseRedirect('/NewspaperDistribution/NewspaperDistributionView/')