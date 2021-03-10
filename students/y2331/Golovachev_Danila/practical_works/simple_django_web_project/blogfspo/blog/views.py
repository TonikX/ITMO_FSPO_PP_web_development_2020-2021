from django.http import Http404, HttpResponse

from django.shortcuts import \
    render  # импортирует метод, который "запускает" созданную хтмл страницу и передает в нее указанные параметры
from .models import *  # импортирует таблицу Poll из модели данных models, где polls - название приложения (и папки)


def detail(request, id):
    try:  # метод try-except - обработчик исключений
        p = CarOwner.objects.get(pk=id)
    except CarOwner.DoesNotExist:
        raise Http404(
            "Poll does not exist")  # исключение которое будет вызвано, если блок try вернет значение False (не будут найдены записи в таблице Poll)

    return render(request, 'blogfspo/detail.html', {
        'owner': p})
