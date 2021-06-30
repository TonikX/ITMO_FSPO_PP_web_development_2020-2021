from datetime import date

from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.contrib import messages

from .forms import *
from .models import *


class ViewAllClubs(View):

    def get(self, request):
        clubs = Club.objects.all()
        return render(request, "clubs/clubs.html", context={"clubs": clubs})


class AddClub(View):

    def get(self, request):
        form = ClubForm()
        return render(request, "clubs/club_add.html", context={"form": form})

    def post(self, request):
        form = ClubForm(request.POST)
        if form.is_valid():
            clubs = Club.objects.all()
            for club in clubs:
                if club.club_name == form.cleaned_data["club_name"]:
                    messages.add_message(request, messages.ERROR, "Клуб с таким названием уже естЬ!")
                    return HttpResponseRedirect('/add_club/')
            Club.objects.create(club_name=form.cleaned_data["club_name"],
                                club_city=form.cleaned_data["club_city"],
                                club_mail=form.cleaned_data["club_mail"],
                                club_phone=form.cleaned_data["club_phone"],
                                country=form.cleaned_data["country"],
                                club_contact_person=form.cleaned_data["club_contact_person"])
            messages.add_message(request, messages.INFO, "Клуб успешно добавлен!")
            return HttpResponseRedirect('/')

        return HttpResponseRedirect('/add_club/')


class DeleteClub(View):

    def get(self, request, club_id):
        club = get_object_or_404(Club, club_id=club_id)
        club.delete()
        messages.add_message(request, messages.INFO, "Клуб успешно удален!")
        return HttpResponseRedirect('/')


class EditClub(View):

    def get(self, request, club_id):
        club = get_object_or_404(Club, club_id=club_id)
        form = ClubForm(initial={
            'club_name': club.club_name,
            'club_city': club.club_city,
            'club_mail': club.club_mail,
            'club_phone': club.club_phone,
            'country': club.country,
            'club_contact_person': club.club_contact_person,
        })

        return render(request, "clubs/club_edit.html", context={"form": form, "club": club})

    def post(self, request, club_id):
        form = ClubForm(request.POST)
        if form.is_valid():
            clubs = Club.objects.all()
            clubing = Club.objects.get(club_id=club_id)
            for club in clubs:
                if clubing.club_name == form.cleaned_data["club_name"]:
                    continue
                if club.club_name == form.cleaned_data["club_name"]:
                    messages.add_message(request, messages.ERROR, "Клуб с таким названием уже есть!")
                    return HttpResponseRedirect('/add_club/')
            Club.objects.filter(club_id=club_id).update(
                club_name=form.cleaned_data["club_name"],
                club_city=form.cleaned_data["club_city"],
                club_mail=form.cleaned_data["club_mail"],
                club_phone=form.cleaned_data["club_phone"],
                country=form.cleaned_data["country"],
                club_contact_person=form.cleaned_data["club_contact_person"])
            messages.add_message(request, messages.INFO, "Клуб обновлен!")
            return HttpResponseRedirect("/")
        messages.add_message(request, messages.INFO, "Неверно введены данные!")
        redirect = '/edit_club/{}'.format(club_id)
        return HttpResponseRedirect(redirect)


class ViewAllClimbers(View):

    def get(self, request):
        climbers = Climber.objects.all()
        return render(request, "climbers/climbers.html", context={"climbers": climbers})


class AddClimber(View):

    def get(self, request):
        form = ClimberForm()
        return render(request, "clubs/club_add.html", context={"form": form})

    def post(self, request):
        form = ClimberForm(request.POST)
        if form.is_valid():
            if int(form.cleaned_data["climber_age"]) <= 0:
                messages.add_message(request, messages.ERROR, "Неправильно введен возраст!")
                return HttpResponseRedirect('/climbers/add')
            if int(form.cleaned_data["climber_xp"]) < 0:
                messages.add_message(request, messages.ERROR, "Неправильно введен опыт альпиниста!")
                return HttpResponseRedirect('/climbers/add')
            club = Club.objects.get(club_name=form.cleaned_data["club"])
            Climber.objects.create(climber_name=form.cleaned_data["climber_name"],
                                climber_surname=form.cleaned_data["climber_surname"],
                                climber_age=form.cleaned_data["climber_age"],
                                climber_xp=form.cleaned_data["climber_xp"],
                                climber_address=form.cleaned_data["climber_address"],
                                club_id=club)
            messages.add_message(request, messages.INFO, "Альпинист успешно добавлен!")
            return HttpResponseRedirect('/climbers/')

        return HttpResponseRedirect('/climbers/add')


class DeleteClimber(View):

    def get(self, request, climber_id):
        climber = get_object_or_404(Climber, climber_id=climber_id)
        climber.delete()
        messages.add_message(request, messages.INFO, "Альпинист успешно удален!")
        return HttpResponseRedirect('/climbers/')


class EditClimber(View):

    def get(self, request, climber_id):
        climber = get_object_or_404(Climber, climber_id=climber_id)
        form = ClimberForm(initial={
            'climber_name': climber.climber_name,
            'climber_surname': climber.climber_surname,
            'climber_age': climber.climber_age,
            'climber_xp': climber.climber_xp,
            'club': climber.club_id,
            'climber_address': climber.climber_address,
        })

        return render(request, "climbers/climber_edit.html", context={"form": form, "climber": climber})

    def post(self, request, climber_id):
        form = ClimberForm(request.POST)
        if form.is_valid():
            if int(form.cleaned_data["climber_age"]) <= 0:
                messages.add_message(request, messages.ERROR, "Неправильно введен возраст!")
                redirect = 'climbers/edit/{}'.format(climber_id)
                return HttpResponseRedirect(redirect)
            if int(form.cleaned_data["climber_xp"]) < 0:
                messages.add_message(request, messages.ERROR, "Неправильно введен опыт альпиниста!")
                redirect = 'climbers/edit/{}'.format(climber_id)
                return HttpResponseRedirect(redirect)
            club = Club.objects.get(club_name=form.cleaned_data["club"])
            Climber.objects.filter(climber_id=climber_id).update(
                climber_name=form.cleaned_data["climber_name"],
                climber_surname=form.cleaned_data["climber_surname"],
                climber_age=form.cleaned_data["climber_age"],
                climber_xp=form.cleaned_data["climber_xp"],
                climber_address=form.cleaned_data["climber_address"],
                club_id=club)
            messages.add_message(request, messages.INFO, "Альпинист обновлен!")
            return HttpResponseRedirect("/climbers/")
        messages.add_message(request, messages.INFO, "Неверно введены данные!")
        redirect = 'climbers/edit/{}'.format(climber_id)
        return HttpResponseRedirect(redirect)


class ViewAllWaypoints(View):

    def get(self, request):
        waypoints = Waypoint.objects.all()
        return render(request, "waypoints/waypoints.html", context={"waypoints": waypoints})


class AddWaypoint(View):

    def get(self, request):
        form = WaypointForm()
        return render(request, "waypoints/waypoint_add.html", context={"form": form})

    def post(self, request):
        form = WaypointForm(request.POST)
        if form.is_valid():
            waypoints = Waypoint.objects.all()
            for waypoint in waypoints:
                if waypoint.waypoint_name == form.cleaned_data["waypoint_name"]:
                    messages.add_message(request, messages.ERROR, "Вершина с таким названием уже естЬ!")
                    return HttpResponseRedirect('/waypoints/add')
            mountain = Mountain.objects.get(mountain_name=form.cleaned_data["mountain"])
            Waypoint.objects.create(waypoint_name=form.cleaned_data["waypoint_name"],
                                waypoint_desc=form.cleaned_data["waypoint_desc"],
                                mountain=mountain)
            messages.add_message(request, messages.INFO, "Вершина обновлена!")
            return HttpResponseRedirect('/waypoints/')

        return HttpResponseRedirect('/waypoints/add')


class DeleteWaypoint(View):

    def get(self, request, waypoint_id):
        waypoint = get_object_or_404(Waypoint, waypoint_id=waypoint_id)
        waypoint.delete()
        messages.add_message(request, messages.INFO, "Вершина успешно удалена!")
        return HttpResponseRedirect('/waypoints/')


class EditWaypoint(View):

    def get(self, request, waypoint_id):
        waypoint = get_object_or_404(Waypoint, waypoint_id=waypoint_id)
        form = WaypointForm(initial={
            'waypoint_name': waypoint.waypoint_name,
            'waypoint_desc': waypoint.waypoint_desc,
            'mountain': waypoint.mountain,
        })

        return render(request, "waypoints/waypoint_edit.html", context={"form": form, "waypoint": waypoint})

    def post(self, request, waypoint_id):
        form = WaypointForm(request.POST)
        if form.is_valid():
            mountain = Mountain.objects.get(mountain_name=form.cleaned_data["mountain"])
            Waypoint.objects.filter(waypoint_id=waypoint_id).update(
                waypoint_name=form.cleaned_data["waypoint_name"],
                waypoint_desc=form.cleaned_data["waypoint_desc"],
                mountain=mountain)
            messages.add_message(request, messages.INFO, "Вершина обновлена!")
            return HttpResponseRedirect("/waypoints/")
        messages.add_message(request, messages.INFO, "Неверно введены данные!")
        redirect = 'waypoints/edit/{}'.format(waypoint_id)
        return HttpResponseRedirect(redirect)


class ViewAllMountains(View):

    def get(self, request):
        mountains = Mountain.objects.all()
        return render(request, "mountains/mountains.html", context={"mountains": mountains})


class ViewWaypointsByMountain(View):
    def get(self, request, mountain_name):
        mountain = get_object_or_404(Mountain, mountain_name=mountain_name)
        waypoints = Waypoint.objects.filter(mountain=mountain)
        string = ""
        if len(waypoints) == 0:
            string = "На этой горе пока нет добавленных вершин"
        return render(request, "waypoints/waypoints.html", context={"waypoints": waypoints, "string": string})


class AddMountain(View):

    def get(self, request):
        form = MountainForm()
        return render(request, "mountains/mountain_add.html", context={"form": form})

    def post(self, request):
        form = MountainForm(request.POST)
        if form.is_valid():
            mountains = Mountain.objects.all()
            for mountain in mountains:
                if mountain.mountain_name == form.cleaned_data["mountain_name"]:
                    messages.add_message(request, messages.ERROR, "Гора с таким названием уже естЬ!")
                    return HttpResponseRedirect('/mountains/add')
            if int(form.cleaned_data["mountain_high"]) < 0:
                messages.add_message(request, messages.ERROR, "Неправильно введена высота горы!")
                return HttpResponseRedirect('/mountains/add')
            Mountain.objects.create(mountain_name=form.cleaned_data["mountain_name"],
                            mountain_high=form.cleaned_data["mountain_high"],
                            country=form.cleaned_data["country"])
            messages.add_message(request, messages.INFO, "Гора успешно добавлена!")
            return HttpResponseRedirect('/mountains/')

        return HttpResponseRedirect('/mountains/add')


class DeleteMountain(View):

    def get(self, request, mountain_id):
        mountain = get_object_or_404(Mountain, mountain_id=mountain_id)
        mountain.delete()
        messages.add_message(request, messages.INFO, "Гора удалена!")
        return HttpResponseRedirect('/mountains/')


def climbing_list(request):
    climbings = Climbing.objects.all()
    for climbing in climbings:
        print(climbing.climbing_finish < datetime.now().date())
        if climbing.climbing_finish < datetime.now().date():
            climbing.status = "Завершен"

        if climbing.climbing_start == datetime.now().date():
            climbing.status = "Выполняется"
        climbing.save()
    return render(request, "climbings/climbings.html", context={"climbings": climbings})


class AddGroupForClimbing(View):

    def get(self, request):
        form = GroupForm()
        return render(request, "groups/group_add.html", context={"form": form})

    def post(self, request):
        form = GroupForm(request.POST)
        if form.is_valid():
            group = Group.objects.create(group_name=form.cleaned_data["group_name"])
            climbers = form.cleaned_data["climber"]
            for climber in climbers:
                group.climber.add(climber)
            group.save()
            redirect = '/climbing/create/{}'.format(group.group_id)
            return HttpResponseRedirect(redirect)

        return HttpResponseRedirect('/climbing/create/group')


class AddClimbing(View):

    def get(self, request, group):
        form = ClimbingForm()
        return render(request, "climbings/climbing_add.html", context={"form": form})


    def post(self, request, group):
        form = ClimbingForm(request.POST)
        if form.is_valid():
            waypoint = Waypoint.objects.get(waypoint_name=form.cleaned_data["waypoint"])
            group = Group.objects.get(group_id=group)
            if form.cleaned_data["climbing_start"] >= form.cleaned_data["climbing_finish"]:
                messages.add_message(request, messages.INFO, "Дата финиша не может быть раньше старта!")
                redirect = '/climbing/create/{}'.format(group)
                return HttpResponseRedirect(redirect)
            Climbing.objects.create(climbing_start=form.cleaned_data["climbing_start"],
                                    climbing_finish=form.cleaned_data["climbing_finish"],
                                    waypoint=waypoint,
                                    group_id=group)

            messages.add_message(request, messages.INFO, "Восхаждение создано!")
            return HttpResponseRedirect("/climbings/")
        messages.add_message(request, messages.INFO, "Неверно введены данные!")
        redirect = '/climbing/create/{}'.format(group)
        return HttpResponseRedirect(redirect)


class CancelClimbing(View):

    def get(self, request, climbing_id):
        climbing = get_object_or_404(Climbing, climbing_id=climbing_id)
        climbing.delete()
        messages.add_message(request, messages.INFO, "Восхождение отменено!")
        return HttpResponseRedirect('/climbings/')


class EditClimbing(View):

    def get(self, request, climbing_id):
        climbing = get_object_or_404(Climbing, climbing_id=climbing_id)
        form = ClimbingForm(initial={
            'climbing_start': climbing.climbing_start,
            'climbing_finish': climbing.climbing_finish,
            'waypoint': climbing.waypoint,
        })

        return render(request, "climbings/climbing_edit.html", context={"form": form})

    def post(self, request, climbing_id):
        form = ClimbingForm(request.POST)
        if form.is_valid():
            waypoint = Waypoint.objects.get(waypoint_name=form.cleaned_data["waypoint"])
            if form.cleaned_data["climbing_start"] >= form.cleaned_data["climbing_finish"]:
                messages.add_message(request, messages.INFO, "Дата финиша не может быть раньше старта!")
                redirect = '/climbings/edit/{}'.format(climbing_id)
                return HttpResponseRedirect(redirect)
            Climbing.objects.filter(climbing_id=climbing_id).update(
                climbing_start=form.cleaned_data["climbing_start"],
                climbing_finish=form.cleaned_data["climbing_finish"],
                waypoint=waypoint)
            messages.add_message(request, messages.INFO, "Восхождение обновлено!")
            return HttpResponseRedirect("/climbings/")
        messages.add_message(request, messages.INFO, "Неверно введены данные!")
        redirect = '/climbings/edit/{}'.format(climbing_id)
        return HttpResponseRedirect(redirect)


class ViewGroupMembers(View):

    def get(self, request, group_id):
        group = Group.objects.get(group_id=group_id)

        return render(request, "groups/group_members.html", context={"group": group})


class EditGroup(View):

    def get(self, request, group_id):
        group = Group.objects.get(group_id=group_id)
        form = AddMembersForm(initial={
            "climber": group.climber.all()
        })
        return render(request, "groups/group_edit.html", context={"form": form})

    def post(self, request, group_id):
        form = AddMembersForm(request.POST)
        if form.is_valid():
            group = Group.objects.filter(group_id=group_id).first()
            climbers = form.cleaned_data["climber"]
            group.climber.clear()
            for climber in climbers:
                group.climber.add(climber)
            group.save()
            messages.add_message(request, messages.INFO, "Группа обновлена!")
            redirect = '/climbing/group/{}'.format(group_id)
            return HttpResponseRedirect(redirect)
        messages.add_message(request, messages.INFO, "Неверно введены данные!")
        redirect = '/climbings/group/edit/{}'.format(group_id)
        return HttpResponseRedirect(redirect)


class ViewGroupInfo(View):

    def get(self, request, group_id):
        group = Group.objects.get(group_id=group_id)

        return render(request, "group_info.html", context={"group": group})


class AddEmergency(View):
    def get(self, request, group_id, climber_id):
        form = EmergencyForm()
        return render(request, "emergency_add.html", context={"form": form})

    def post(self, request, group_id, climber_id):
        form = EmergencyForm(request.POST)
        if form.is_valid():
            climber = Climber.objects.get(climber_id=climber_id)
            emergency = EmergencySituation.objects.create(desc=form.cleaned_data["desc"], climber=climber)
            group = Group.objects.filter(group_id=group_id).first()
            group.emergency.add(emergency)
            group.save()
            redirect = '/climbing/group/info/{}'.format(group_id)
            return HttpResponseRedirect(redirect)

        redirect = '/climbing/group/emergency/{}'.format(group_id)
        return HttpResponseRedirect(redirect)