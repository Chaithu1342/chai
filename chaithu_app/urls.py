from django.urls import path
from chaithu_app import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("", views.index, name="index"),  # Home page
    path("signup/", views.signup, name="signup"),
    path("login/", views.user_login, name="login"),
    path("logout/", LogoutView.as_view(next_page="login"), name="logout"), 
    path("dashboard/", views.dashboard, name="dashboard"),
    path("profile/", views.profile, name="profile"),
    path("reports/", views.reports, name="reports"),
    path("settings/", views.settings, name="settings"),
]
