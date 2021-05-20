import datetime

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import F
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.views.generic import CreateView, ListView, DeleteView, UpdateView

from labor_app.forms import JoblessForm, OrganizationForm, StipendForm, ProgramForm, GroupForm, PassageForm, \
    JoblessEditForm
from labor_app.models import Jobless, EducationalOrganization, Stipend, EducationalProgram, EducationalGroup, Passage


def my_groups_list(request):
    user = request.user
    if user.is_authenticated:
        jobless = Jobless.objects.get(username=user.username)
        passages = Passage.objects.filter(jobless=jobless, statofadopt=True).values_list('group', flat=True)
        groups = EducationalGroup.objects.filter(id__in=passages)
        paginator = Paginator(groups, 8)
        page = request.GET.get('page')
        if (page):
            page = int(page)
        try:
            groups = paginator.page(page)
        except PageNotAnInteger:
            page = int(1)
            groups = paginator.page(1)
        except EmptyPage:
            groups = paginator.page(paginator.num_pages)
        return render(request, 'myGroups.html', context={'object_list': groups,'page':page})
    else:
        return HttpResponse("<h1>You are not authenticated</h1>")


def leave_group(request, pk):
    user = request.user
    if user.is_authenticated:
        jobless = Jobless.objects.get(username=user.username)
        passage = Passage.objects.get(jobless=jobless, group=pk)
        passage.delete()
        return HttpResponseRedirect('/MyGroups/List')
    else:
        return HttpResponse("<h1>You are not authenticated</h1>")


def delete_user(request):
    user = request.user
    jobless = Jobless.objects.get(username=user.username)
    jobless.is_active = False
    jobless.save()
    return HttpResponseRedirect('/LogOut/')


def registration(request):
    user_form = JoblessForm(request.POST or None)
    if user_form.is_valid():
        # Create a new user object but avoid saving it yet
        new_user = user_form.save(commit=False)
        # Set the chosen password
        new_user.set_password(user_form.cleaned_data['password'])
        # Save the User object
        new_user.save()
        return HttpResponseRedirect('/login/')

    else:
        user_form = JoblessForm()
        return render(request, 'createJobless.html', {'form': user_form})


def getAction(request):
    return render(request, 'home.html')


def detail_jobless(request):
    if request.user.is_authenticated:
        jl = Jobless.objects.get(username=request.user.username)
        return render(request, 'joblessDetail.html', context={'object': jl})
    else:
        return HttpResponse("<h1>User does not exist</h1>")


def avial_groups(request):
    grps = list(EducationalGroup.objects.all())
    for g in grps:
        g.studquan = Passage.objects.filter(group=g).count()
        g.save()
    jobless = Jobless.objects.get(username=request.user.username)
    programs = EducationalProgram.objects.filter(startdate__lt=datetime.datetime.now(),finishdate__gt=datetime.datetime.now())
    groups = EducationalGroup.objects.filter(program__in=programs, studquan__lt=F('maxquanstud')).exclude(id__in=Passage.objects.filter(jobless=jobless).values_list('group_id', flat=True)).order_by('id')
    paginator = Paginator(groups, 2);
    page = request.GET.get('page')
    if (page):
        page = int(page)
    try:
        groups = paginator.page(page)
    except PageNotAnInteger:
        page = int(1)
        groups = paginator.page(1)
    except EmptyPage:
        groups = paginator.page(paginator.num_pages)
    return render(request, 'AvailGroupsList.html', context={'programs': programs, 'groups': groups,'page':page})


def view_member(request, g_id):
    passages = Passage.objects.filter(group__id=g_id)
    return render(request, 'viewMember.html', context={'object': passages})


def join_group(request, pk):
    group = EducationalGroup.objects.get(id=pk)
    if not Passage.objects.filter(jobless=Jobless.objects.get(username=request.user.username), group=group).exists():
        if request.user.is_authenticated:
            jobless = Jobless.objects.get(username=request.user.username)
            new_pass = Passage()
            new_pass.group = group
            new_pass.jobless = jobless
            new_pass.statofadopt = False
            new_pass.document = False
            new_pass.save()
            if group.studquan < group.maxquanstud:
                group.studquan += 1
                group.save(update_fields=["studquan"])
                return HttpResponseRedirect('/AvailGroups/List')
            return HttpResponse("<h1>User is not authenticated</h1>")
    return HttpResponse("<h1>Passage with this group already exists</h1>")


# Working with organization
class OrganizationList(ListView):
    model = EducationalOrganization
    template_name = 'organizationList.html'

    def get(self, request, *args, **kwargs):
        user = request.user
        if user.is_authenticated:
            if user.is_superuser:
                object_list = EducationalOrganization.objects.all().order_by('id')
                paginator = Paginator(object_list, 8)
                page = request.GET.get('page')
                if(page):
                    page=int(page)
                try:
                    object_list = paginator.page(page)
                except PageNotAnInteger:
                    page=int(1)
                    object_list = paginator.page(1)
                except EmptyPage:
                    object_list = paginator.page(paginator.num_pages)
                return render(self.request, 'organizationList.html', context={'object_list': object_list,'page':page})
            else:
                return HttpResponse("<h1>You are not admin</h1>")
        else:
            return HttpResponse("<h1>You are not authenticated</h1>")


class OrganizationCreate(CreateView):
    model = EducationalOrganization
    template_name = 'organizationCreate.html'
    success_url = '/Organization/List'
    fields = ['name', 'type', 'address']

    def get(self, request, *args, **kwargs):
        user = request.user
        if user.is_authenticated:
            if user.is_superuser:
                return render(self.request, 'organizationCreate.html', context={'form': self.get_form_class()})
            else:
                return HttpResponse("<h1>You are not admin</h1>")
        else:
            return HttpResponse("<h1>You are not authenticated</h1>")


class OrganizationDelete(DeleteView):
    model = EducationalOrganization
    template_name = 'organizationDelete.html'
    success_url = '/Organization/List'

    def get(self, request, *args, **kwargs):
        user = request.user
        if user.is_authenticated:
            if user.is_superuser:
                return render(self.request, 'organizationDelete.html', context={'object': self.get_object})
            else:
                return HttpResponse("<h1>You are not admin</h1>")
        else:
            return HttpResponse("<h1>You are not authenticated</h1>")


class JoblessUpdate(UpdateView):
    model = Jobless
    template_name = 'updateJobless.html'
    form_class = JoblessEditForm


class OrganizationUpdate(UpdateView):
    model = EducationalOrganization
    template_name = 'organizationUpdate.html'
    success_url = '/Organization/List'
    form_class = OrganizationForm

    def get(self, request, pk):
        user = request.user
        if user.is_authenticated:
            if user.is_superuser:
                return render(self.request, 'organizationUpdate.html',
                              context={'form': self.form_class(instance=EducationalOrganization.objects.get(id=pk))})
            else:
                return HttpResponse("<h1>You are not admin</h1>")
        else:
            return HttpResponse("<h1>You are not authenticated</h1>")


# Working with stipend
class StipendCreate(CreateView):
    model = Stipend
    template_name = 'stipendCreate.html'
    form_class = StipendForm
    success_url = '/Stipend/List'

    def get(self, request, *args, **kwargs):
        user = request.user
        if user.is_authenticated:
            if user.is_superuser or user.is_staff:
                return render(self.request, 'stipendCreate.html', context={'form': self.get_form_class()})
            else:
                return HttpResponse("<h1>You are not admin</h1>")
        else:
            return HttpResponse("<h1>You are not authenticated</h1>")


class StipendUpdate(UpdateView):
    model = Stipend
    template_name = 'stipendUpdate.html'
    success_url = '/Stipend/List'
    form_class = StipendForm

    def get(self, request, pk):
        user = request.user
        if user.is_authenticated:
            if user.is_superuser or user.is_staff:
                return render(self.request, 'stipendUpdate.html',
                              context={'form': self.form_class(instance=Stipend.objects.get(id=pk))})
            else:
                return HttpResponse("<h1>You are not admin</h1>")
        else:
            return HttpResponse("<h1>You are not authenticated</h1>")


class JoblessList(ListView):
    model = Jobless
    template_name = 'joblessList.html'

    def get(self, request, *args, **kwargs):
        user = request.user
        if user.is_authenticated:
            if user.is_superuser:
                object_list = Jobless.objects.exclude(username=user.username).order_by('id')
                paginator = Paginator(object_list, 4)
                page = request.GET.get('page')
                if (page):
                    page = int(page)
                try:
                    object_list = paginator.page(page)
                except PageNotAnInteger:
                    page = int(1)
                    object_list = paginator.page(1)
                except EmptyPage:
                    object_list = paginator.page(paginator.num_pages)
                return render(self.request, 'joblessList.html', context={'object_list': object_list, 'page': page})
            else:
                return HttpResponse("<h1>You are not admin</h1>")
        else:
            return HttpResponse("<h1>You are not authenticated</h1>")


class StipendDelete(DeleteView):
    model = Stipend
    template_name = 'stipendDelete.html'
    success_url = '/Stipend/List'

    def get(self, request, *args, **kwargs):
        user = request.user
        if user.is_authenticated:
            if user.is_superuser or user.is_staff:
                return render(self.request, 'stipendDelete.html', context={'object': self.get_object()})
            else:
                return HttpResponse("<h1>You are not admin</h1>")
        else:
            return HttpResponse("<h1>You are not authenticated</h1>")


class StipendList(ListView):
    model = Stipend
    template_name = 'stipendList.html'

    def get(self, request, *args, **kwargs):
        user = request.user
        if user.is_authenticated:
            if user.is_superuser or user.is_staff:
                object_list=Stipend.objects.all().order_by('id')
                paginator = Paginator(object_list, 8)
                page = request.GET.get('page')
                if (page):
                    page = int(page)
                try:
                    object_list = paginator.page(page)
                except PageNotAnInteger:
                    page = int(1)
                    object_list = paginator.page(1)
                except EmptyPage:
                    object_list = paginator.page(paginator.num_pages)
                return render(self.request, 'stipendList.html', context={'object_list': object_list, 'page': page})
            else:
                return HttpResponse("<h1>You are not admin</h1>")
        else:
            return HttpResponse("<h1>You are not authenticated</h1>")


# Working with group
class ProgramCreate(CreateView):
    model = EducationalProgram
    template_name = 'programCreate.html'
    form_class = ProgramForm
    success_url = '/Program/List'

    def get(self, request, *args, **kwargs):
        user = request.user
        if user.is_authenticated:
            if user.is_superuser:
                return render(self.request, 'programCreate.html', context={'form': self.get_form_class()})
            else:
                return HttpResponse("<h1>You are not admin</h1>")
        else:
            return HttpResponse("<h1>You are not authenticated</h1>")


class ProgramUpdate(UpdateView):
    model = EducationalProgram
    template_name = 'programUpdate.html'
    form_class = ProgramForm
    success_url = '/Program/List'

    def get(self, request, pk):
        user = request.user
        if user.is_authenticated:
            if user.is_superuser:
                return render(self.request, 'programUpdate.html',
                              context={'form': self.form_class(instance=EducationalProgram.objects.get(id=pk))})
            else:
                return HttpResponse("<h1>You are not admin</h1>")
        else:
            return HttpResponse("<h1>You are not authenticated</h1>")


class ProgramDelete(DeleteView):
    model = EducationalProgram
    template_name = 'programDelete.html'
    success_url = '/Program/List'

    def get(self, request, *args, **kwargs):
        user = request.user
        if user.is_authenticated:
            if user.is_superuser:
                return render(self.request, 'programDelete.html', context={'object': self.get_object()})
            else:
                return HttpResponse("<h1>You are not admin</h1>")
        else:
            return HttpResponse("<h1>You are not authenticated</h1>")


class ProgramList(ListView):
    model = EducationalProgram
    template_name = 'programList.html'

    def get(self, request, *args, **kwargs):
        user = request.user
        if user.is_authenticated:
            if user.is_superuser:
                object_list=EducationalProgram.objects.all().order_by('id')
                paginator = Paginator(object_list, 4)
                page = request.GET.get('page')
                if (page):
                    page = int(page)
                try:
                    object_list = paginator.page(page)
                except PageNotAnInteger:
                    page = int(1)
                    object_list = paginator.page(1)
                except EmptyPage:
                    object_list = paginator.page(paginator.num_pages)
                return render(self.request, 'programList.html', context={'object_list': object_list, 'page': page})
            else:
                return HttpResponse("<h1>You are not admin</h1>")
        else:
            return HttpResponse("<h1>You are not authenticated</h1>")


# Working with Edu group
class GroupCreate(CreateView):
    model = EducationalGroup
    template_name = 'groupCreate.html'
    fields = ['program', 'maxquanstud']
    success_url = '/Group/List'

    def get(self, request, *args, **kwargs):
        user = request.user
        if user.is_authenticated:
            if user.is_superuser:
                return render(self.request, 'groupCreate.html', context={'form': self.get_form_class()})
            else:
                return HttpResponse("<h1>You are not admin</h1>")
        else:
            return HttpResponse("<h1>You are not authenticated</h1>")


class GroupUpdate(UpdateView):
    model = EducationalGroup
    template_name = 'groupUpdate.html'
    form_class = GroupForm
    success_url = '/Group/List'

    def get(self, request, pk):
        user = request.user
        if user.is_authenticated:
            if user.is_superuser:
                return render(self.request, 'groupUpdate.html',
                              context={'form': self.form_class(instance=EducationalGroup.objects.get(id=pk))})
            else:
                return HttpResponse("<h1>You are not admin</h1>")
        else:
            return HttpResponse("<h1>You are not authenticated</h1>")


class GroupDelete(DeleteView):
    model = EducationalGroup
    template_name = 'groupDelete.html'
    success_url = '/Group/List'

    def get(self, request, *args, **kwargs):
        user = request.user
        if user.is_authenticated:
            if user.is_superuser:
                return render(self.request, 'groupDelete.html', context={'object': self.get_object()})
            else:
                return HttpResponse("<h1>You are not admin</h1>")
        else:
            return HttpResponse("<h1>You are not authenticated</h1>")


class GroupList(ListView):
    model = EducationalGroup
    template_name = 'groupList.html'

    def get(self, request, *args, **kwargs):
        user = request.user
        if user.is_authenticated:
            if user.is_superuser:
                groups = list(EducationalGroup.objects.all())
                for g in groups:
                    g.studquan = Passage.objects.filter(group=g).count()
                    g.save()
                object_list=EducationalGroup.objects.all().order_by('id')
                paginator = Paginator(object_list, 8)
                page = request.GET.get('page')
                if (page):
                    page = int(page)
                try:
                    object_list = paginator.page(page)
                except PageNotAnInteger:
                    page = int(1)
                    object_list = paginator.page(1)
                except EmptyPage:
                    object_list = paginator.page(paginator.num_pages)
                return render(self.request, 'groupList.html', context={'object_list': object_list, 'page': page})
            else:
                return HttpResponse("<h1>You are not admin</h1>")
        else:
            return HttpResponse("<h1>You are not authenticated</h1>")


class PassageList(ListView):
    model = Passage
    template_name = 'passageList.html'

    def get(self, request, *args, **kwargs):
        user = request.user
        if user.is_authenticated:
            if user.is_superuser or user.is_staff:
                object_list = Passage.objects.all().order_by('id')
                paginator = Paginator(object_list, 8)
                page = request.GET.get('page')
                if (page):
                    page = int(page)
                try:
                    object_list = paginator.page(page)
                except PageNotAnInteger:
                    page = int(1)
                    object_list = paginator.page(1)
                except EmptyPage:
                    object_list = paginator.page(paginator.num_pages)
                return render(self.request, 'passageList.html', context={'object_list': object_list, 'page': page})
            else:
                return HttpResponse("<h1>You are not admin</h1>")
        else:
            return HttpResponse("<h1>You are not authenticated</h1>")


class PassageCreate(CreateView):
    model = Passage
    template_name = 'passageCreate.html'
    form_class = PassageForm
    success_url = '/Passage/List'

    def get(self, request, *args, **kwargs):
        user = request.user
        if user.is_authenticated:
            if user.is_superuser or user.is_staff:
                return render(self.request, 'passageCreate.html', context={'form': self.get_form_class()})
            else:
                return HttpResponse("<h1>You are not admin</h1>")
        else:
            return HttpResponse("<h1>You are not authenticated</h1>")


class PassageDelete(DeleteView):
    model = Passage
    template_name = 'passageDelete.html'
    success_url = '/Passage/List'

    def get(self, request, *args, **kwargs):
        user = request.user
        if user.is_authenticated:
            if user.is_superuser or user.is_staff:
                return render(self.request, 'passageDelete.html', context={'object': self.get_object()})
            else:
                return HttpResponse("<h1>You are not admin</h1>")
        else:
            return HttpResponse("<h1>You are not authenticated</h1>")


class PassageUpdate(UpdateView):
    model = Passage
    template_name = 'passageUpdate.html'
    form_class = PassageForm
    success_url = '/Passage/List'

    def get(self, request, pk):
        user = request.user
        if user.is_authenticated:
            if user.is_superuser or user.is_staff:
                return render(self.request, 'passageUpdate.html',
                              context={'form': self.form_class(instance=Passage.objects.get(id=pk))})
            else:
                return HttpResponse("<h1>You are not admin</h1>")
        else:
            return HttpResponse("<h1>You are not authenticated</h1>")
