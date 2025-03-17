from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.decorators.csrf import ensure_csrf_cookie

# ✅ First Page (Index)
def index(request):
    return render(request, "chaithu_app/index.html")  # Ensure index.html exists

# ✅ User Signup
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
        user.save()
        login(request, user)
        messages.success(request, "Signup successful! Redirecting to dashboard.")
        return redirect("dashboard")

    return render(request, "chaithu_app/signup.html")

# ✅ User Login
@ensure_csrf_cookie  # Ensures CSRF token is included in login page
def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("dashboard")
        else:
            messages.error(request, "Invalid username or password.")

    form = AuthenticationForm()
    return render(request, "chaithu_app/login.html", {"form": form})

# ✅ User Logout
def user_logout(request):
    logout(request)
    return redirect("index")  # Redirect to index after logout

# ✅ Dashboard (Requires Login)
@login_required
def dashboard(request):
    return render(request, "chaithu_app/dashboard.html")

# ✅ Profile (Requires Login)
@login_required
def profile(request):
    return render(request, "chaithu_app/profile.html")

# ✅ Reports (Requires Login)
@login_required
def reports(request):
    return render(request, "chaithu_app/reports.html")

# ✅ Settings (Requires Login)
@login_required
def settings(request):
    return render(request, "chaithu_app/settings.html")
