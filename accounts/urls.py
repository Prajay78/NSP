from django.urls.conf import path, re_path, include
from accounts import views
from django.contrib.auth.views import (
    logout,
    password_reset,
    password_reset_done,
    password_reset_confirm,
    password_reset_complete,
)
from django.contrib.auth import views as auth_views
from accounts.views import EditUserProfileView

urlpatterns = [
    path("change_profilepic", views.ChangeProfilePicture, name="ChangeProfilePicture"),
    path('testing/', views.django_image_and_file_upload_ajax, name='testing'),
    path('', views.HomeView, name='home'),
    path('delete/<type_>/<ID>', views.deleteIssueSolution, name="deleteIssueSolution"),
    path('project/delete/<ID>', views.deleteProject, name="deleteProject"),
    path('project/start/', views.ProjectDescribeView, name='start_project'),
    path('project/active/', views.ProjectsListView, name='project_list_view'),
    path("project/interested/<ID>", views.interestedList, name="interestedList"),
    path("project/addInterested/<ID>", views.addInterested, name="addInterested"),
    path("project/active/removeInsterested/<ID>", views.removeInsterested, name="removeInsterested"),
    path('project/<ID>/edit', views.projectEdit, name='projectEdit'),
    path('project/<project_id>/', views.ProjectDetailView, name='view_project_detail'),
    path('project/<ID>/issues/<status>', views.projectIssues, name='projectIssues'),
    path('project/<ID>/solutions/<status>', views.projectSolutions, name='projectSolutions'),
    path('project/<projectID>/<type_>/<ID>/edit', views.editIssueSolution, name='editIssueSolution'),
    path('project/<projectID>/<type_>/create', views.createIssueSolution, name='createIssueSolution'),
    path('project/<projectID>/<type_>/<ID>', views.viewIssueSolution, name='viewIssueSolution'),
    path('project/<projectID>/<type_>/<ID>/<status>', views.changeStatusIssueSolution, name='changeStatusIssueSolution'),
    path('project/<projectID>/<type_>/<ID>/comment', views.commentIssueSolution, name='commentIssueSolution'),
    path('login/', auth_views.login, {'template_name': 'accounts/login.html'}, name='user_login'),
    path('registersuccess/', views.SuccesfullRegistrationView, name='registersucess'),
    path('register/', views.RegistrationView, name='signup'),
    path('logout/', logout, {'template_name': 'accounts/logout.html'}, name='logout'),
    path('profile/', views.ProfileView, name='view_profile'),
    path('people/', views.PeopleView, name='view_people'),
    path("social/follow/<ID>", views.followUser, name="followUser"),
    path("social/unfollow/<ID>", views.unfollowUser, name="unfollowUser"),
    path('users/<username>', views.FriendProfileView, name='view_friend'),
    path('profile/skills', views.SkillsView, name='skills'),
    path('profile/edit', views.EditProfileView, name='edit_profile'),
    re_path('profile/(?P<pk>\d+)/edit_details', EditUserProfileView.as_view(), name='EditDetails'),
    path('change-password/', views.ChangePasswordView, name='change_password'),
    path('reset-password/', password_reset, name='reset_password'),
    path('reset-password/done/', password_reset_done, name='password_reset_done'),
    re_path('reset-password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/', password_reset_confirm,
            name='password_reset_confirm'),
    path('reset-password/complete/', password_reset_complete, name='password_reset_complete'),
    path('profile/addskill/', views.AddSkillView, name='addskill'),
    path('profile/deleteskill/<ID>', views.deleteSkill, name='deleteskill'),
    path('search/', views.search, name='search'),
]
