from django.shortcuts import render
# импортирует метод, который "запускает" созданную хтмл страницу и передает в нее указанные параметры

from django.http import Http404
# импортирует метод обработки ситуации, когда нет    необходимых записей в бд (обработчик ошибок)

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView

from .models import Owner
from .models import Auto

from .forms import OwnerForm


def detail_owner(request, owner_id):
    try:  # метод try-except - обработчик исключений
        p = Owner.objects.get(
            pk=owner_id)

    # pk - автоматически создается в джанго для любой таблицы в моделе (оно есть у любого объекта из бд),
    # poll_id будет передан функции при её вызове. переменной p присваивается объект, полученный в результате
    # выполнения запроса аналогичного "select * from Poll where pk=poll_id"
    except Owner.DoesNotExist:
        raise Http404(
            "Owner does not exist")
        # исключение которое будет вызвано, если блок try вернет значение False (не
        # будут найдены записи в таблице Poll)
    return render(request, 'first_app/owner.html', {
        'owner': p})
    # данная строка рендерит хтмл страницу detail.html и передает в него объект "p", который в хтмл
    # шаблоне будет называться "poll"


def list_view_owner(request):
    # dictionary for initial data with
    # field names as keys
    context = {"dataset": Owner.objects.all()}

    # add the dictionary during initialization [en]
    # добавление данных об объектах, полученных в результате выполнения запроса exampleModel.objects.all() в словарь

    return render(request, "first_app/owner_list_view.html", context)


def create_view_owner(request):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization
    form = OwnerForm(
        request.POST or None)  # создание экземпляра формы, передача в него данных из формы (из полей в браузере)
    if form.is_valid():  # проверка формы на корректность (валидация)
        form.save()
    context['form'] = form
    return render(request, "first_app/owner_create_view.html", context)


class AutoList(ListView):
    # specify the model for list view
    model = Auto
    template_name = 'first_app/cvb_list_view.html'


class AutoRetrieveView(DetailView):
    model = Auto


class AutoUpdateView(UpdateView):
    model = Auto
    fields = ['number', 'brand', 'model', 'color']
    success_url = 'first_app/auto/list'


class AutoCreateView(CreateView):
    # specify the model for create view
    model = Auto
    template_name = 'first_app/cvb_create_view.html'

    # specify the fields to be displayed

    fields = ['number', 'brand', 'model', 'color']


class AutoDeleteView(DeleteView):
    # specify the model for create view
    model = Auto
    success_url = 'first_app/auto/list'

