from django.urls import path
from .views import *

urlpatterns = [
    path("", ViewAllClubs.as_view(), name="all_clubs"),
    path("add_club/", AddClub.as_view(), name="add_club"),
    path("edit_club/<int:club_id>", EditClub.as_view(), name="edit_club"),
    path("delete_club/<int:club_id>", DeleteClub.as_view(), name="delete_club"),

    path("climbers/", ViewAllClimbers.as_view(), name="all_climbers"),
    path("climbers/add", AddClimber.as_view(), name="add_climber"),
    path("climbers/delete/<int:climber_id>", DeleteClimber.as_view(), name="delete_climber"),
    path("climbers/edit/<int:climber_id>", EditClimber.as_view(), name="edit_climber"),

    path("waypoints/", ViewAllWaypoints.as_view(), name="all_waypoints"),
    path("waypoints/add", AddWaypoint.as_view(), name="add_waypoint"),
    path("waypoints/delete/<int:waypoint_id>", DeleteWaypoint.as_view(), name="delete_waypoint"),
    path("waypoints/edit/<int:waypoint_id>", EditWaypoint.as_view(), name="edit_waypoint"),

    path("mountains/", ViewAllMountains.as_view(), name="all_mountains"),
    path("mountains/<str:mountain_name>/waypoints/", ViewWaypointsByMountain.as_view(), name="mountain_waypoints"),
    path("mountains/add", AddMountain.as_view(), name="add_mountain"),
    path("mountains/delete/<int:mountain_id>", DeleteMountain.as_view(), name="delete_mountain"),

    path("climbings/", climbing_list, name="all_climbings"),
    path("climbing/create/group", AddGroupForClimbing.as_view(), name="create_group"),
    path("climbing/create/<int:group>", AddClimbing.as_view(), name="create_climbing"),
    path("climbings/cancel/<int:climbing_id>", CancelClimbing.as_view(), name="cancel_climbing"),
    path("climbings/edit/<int:climbing_id>", EditClimbing.as_view(), name="edit_climbing"),
    path("climbing/group/<int:group_id>", ViewGroupMembers.as_view(), name="all_group_members"),
    path("climbings/group/edit/<int:group_id>", EditGroup.as_view(), name="edit_group"),

    path("climbing/group/info/<int:group_id>", ViewGroupInfo.as_view(), name="group_info"),
    path("climbing/group/emergency/<int:group_id>/<int:climber_id>", AddEmergency.as_view(), name="add_emergency"),
]