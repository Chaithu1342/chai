from django.contrib import admin
from django.urls import path
from chaithu_app.views import (
    index, signup, user_login, user_logout, 
    dashboard, profile, reports, settings
)

urlpatterns = [
    path("", index, name="index"),
    path("signup/", signup, name="signup"),
    path("login/", user_login, name="login"),
    path("logout/", user_logout, name="logout"),
    path("dashboard/", dashboard, name="dashboard"),
    path("profile/", profile, name="profile"),
    path("reports/", reports, name="reports"),
    path("settings/", settings, name="settings"),
    path("admin/", admin.site.urls),  # ✅ Keep this to access Django admin
]
