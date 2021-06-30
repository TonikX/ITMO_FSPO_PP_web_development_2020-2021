from django.urls import path
from .views import *

app_name = "hack"

urlpatterns = [
    path('index/', index, name='index'),
    path('login/', login, name='login-form'),
    path('signup/', signup, name='signup-form'),

    path('member/create', TeamMemberCreateAPIView.as_view()),
    path('member/update/<int:pk>', TeamMemberUpdateAPIView.as_view()),  # iscaptain
    path('member/delete/<int:pk>', TeamMemberDeleteAPIView.as_view()),  # iscaptain

    path('captain/get/<int:pk>', CaptainGetAPIView.as_view()),

    path('issue/list', IssueListAPIView.as_view()),
    path('issue/update/<int:pk>', IssueUpdateAPIView.as_view()),  # ismentor or isadmin
    path('issue/get/<int:pk>', IssueGetAPIView.as_view()),  # isauth
    path('issue/delete/<int:pk>', IssueDeleteAPIView.as_view()),  # isadmin
    path('issue/create', IssueCreateAPIView.as_view()),  # isadmin

    path('team/list', TeamListAPIView.as_view()),
    path('team/create', TeamCreateAPIView.as_view()),
    path('team/update/<int:pk>', TeamUpdateAPIView.as_view()),  # iscaptain
    path('team/delete/<int:pk>', TeamDeleteAPIView.as_view()),  # iscaptain

    path('solution/list', SolutionListAPIView.as_view()),
    path('solution/create', SolutionCreateAPIView.as_view()),  # is abstract captain
    path('solution/update/<int:pk>', SolutionUpdateAPIView.as_view()),  # isjury
    path('solution/delete/<int:pk>', SolutionDeleteAPIView.as_view()),  # iscaptain
]
