from django.contrib.auth import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include

from labor_app import views

urlpatterns = [
    path('home/', views.getAction),
    path('SignUp/', views.registration),
    path('', include('django.contrib.auth.urls')),
    path('LogOut/',LogoutView.as_view(),name="logout"),
    path('Jobless/Detail/',views.detail_jobless),

    path('Organization/List',views.OrganizationList.as_view()),
    path('Organization/Update/<int:pk>',views.OrganizationUpdate.as_view()),
    path('Organization/Delete/<int:pk>',views.OrganizationDelete.as_view()),
    path('Organization/Create',views.OrganizationCreate.as_view()),

    path('Stipend/List',views.StipendList.as_view()),
    path('Stipend/Update/<int:pk>',views.StipendUpdate.as_view()),
    path('Stipend/Delete/<int:pk>',views.StipendDelete.as_view()),
    path('Stipend/Create',views.StipendCreate.as_view()),

    path('Program/List',views.ProgramList.as_view()),
    path('Program/Update/<int:pk>',views.ProgramUpdate.as_view()),
    path('Program/Delete/<int:pk>',views.ProgramDelete.as_view()),
    path('Program/Create',views.ProgramCreate.as_view()),

    path('Group/List',views.GroupList.as_view()),
    path('Group/Update/<int:pk>',views.GroupUpdate.as_view()),
    path('Group/Delete/<int:pk>',views.GroupDelete.as_view()),
    path('Group/Create',views.GroupCreate.as_view()),

    path('AvailGroups/List/',views.avial_groups),
    path('JoinGroup/<int:pk>',views.join_group),

    path('Passage/List',views.PassageList.as_view()),
    path('Passage/Create',views.PassageCreate.as_view()),
    path('Passage/Delete/<int:pk>',views.PassageDelete.as_view()),
    path('Passage/Update/<int:pk>', views.PassageUpdate.as_view()),

    path('ViewMember/<int:g_id>',views.view_member),
    path('MyGroups/List', views.my_groups_list),
    path('LeaveGroup/<int:pk>',views.leave_group),

    path('Jobless/List',views.JoblessList.as_view()),
    path('Jobless/Update/<int:pk>',views.JoblessUpdate.as_view(success_url='/Jobless/Detail')),

    path('DeleteUser',views.delete_user)

]