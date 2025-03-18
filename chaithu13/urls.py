from django.urls import path
from chaithu_app import views  # Import views from your app

urlpatterns = [
    path("", views.index, name="index"),  # ✅ First page should be "index"
    path("signup/", views.signup, name="signup"),
    path("login/", views.user_login, name="login"),
    path("logout/", views.user_logout, name="logout"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("profile/", views.profile, name="profile"),
    path("reports/", views.reports, name="reports"),
    path("settings/", views.settings, name="settings"),
]
from django.contrib.auth.views import LoginView

urlpatterns = [
    path("login/", LoginView.as_view(template_name="login.html"), name="login"),
]
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    return render(request, "dashboard.html")
