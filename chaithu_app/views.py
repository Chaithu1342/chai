from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.csrf import ensure_csrf_cookie
from django.contrib.auth.models import User

# ✅ Home Page
def index(request):
    return render(request, "chaithu_app/index.html")

# ✅ Signup View
def signup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        if password != confirm_password:
            messages.error(request, "Passwords do not match!")
            return redirect("signup")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken!")
            return redirect("signup")

        user = User.objects.create_user(username=username, password=password)
        login(request, user)  # ✅ Auto-login after signup
        messages.success(request, "Signup successful!")
        return redirect("dashboard")  # ✅ Redirect to dashboard after signup

    return render(request, "chaithu_app/signup.html")

# ✅ Login View
@ensure_csrf_cookie  
def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Login successful!")
            return redirect("dashboard")  # ✅ Redirect to dashboard after login
        else:
            messages.error(request, "Invalid username or password")

    return render(request, "chaithu_app/login.html")

# ✅ Logout View
def user_logout(request):
    logout(request)
    return redirect("index")  # ✅ Redirect to home after logout

# ✅ Dashboard View (Requires Login)
@login_required
def dashboard(request):
    return render(request, "chaithu_app/dashboard.html")

# ✅ Profile View (Requires Login)
@login_required
def profile(request):
    return render(request, "chaithu_app/profile.html")

# ✅ Reports View (Requires Login)
@login_required
def reports(request):
    return render(request, "chaithu_app/reports.html")

# ✅ Settings View (Requires Login)
@login_required
def settings(request):
    return render(request, "chaithu_app/settings.html")
