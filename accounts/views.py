from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST, require_http_methods

from django.contrib.auth.forms import AuthenticationForm # 로그인 폼
from django.contrib.auth import login as auth_login # 로그인
from django.contrib.auth import logout as auth_logout # 로그아웃


from .forms import UserForm
# Create your views here.


def testhome(request):
    return render(request, "accounts/testhome.html")


@require_http_methods(["POST", "GET"])
def login(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect("accounts:test")

    form = AuthenticationForm()
    return render(request, "accounts/login.html", {"form": form})


# @require_http_methods(["GET", "POST"])
# def signup(request):
#     if request.method == "POST":
#
#     form = UserForm()
#     return render(request, "accounts/signup.html", {"form": form})
