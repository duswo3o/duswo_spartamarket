from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST, require_http_methods

from django.contrib.auth.forms import AuthenticationForm # 로그인 폼
from django.contrib.auth import login as auth_login # 로그인
from django.contrib.auth import logout as auth_logout # 로그아웃


from .forms import CustomUserCreationForm, CustomUserChangeForm
# Create your views here.


@require_http_methods(["POST", "GET"])
def login(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect("products:index")

    form = AuthenticationForm()
    return render(request, "accounts/login.html", {"form": form})


@require_POST
def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
    return redirect("products:index")


@require_http_methods(["GET", "POST"])
def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect("products:index")

    form = CustomUserCreationForm()
    return render(request, "accounts/signup.html", {"form": form})


@require_http_methods(["GET", "POST"])
def update(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            form = CustomUserChangeForm(request.POST, instance=request.user)
            form.save()
            return redirect("products:index")

    form = CustomUserChangeForm()
    return render(request, "accounts/update.html", {"form":form})


@require_POST
def delete(request):
    if request.user.is_authenticated:
        request.user.delete()
        auth_logout(request)
        return redirect("products:index")