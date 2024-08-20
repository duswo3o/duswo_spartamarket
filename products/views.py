from django.shortcuts import render, redirect

from django.views.decorators.http import require_http_methods, require_POST
# from django.contrib.auth import

from .models import Post
from .forms import PostForm
# Create your views here.


def index(request):
    # form = PostForm()
    posts = Post.objects.all()

    context = {
        # "form": form,
        "posts": posts,
    }
    return render(request, "products/index.html", context)


@require_http_methods(["GET", "POST"])
def create(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            form = PostForm()
            return render(request, "products/create.html", {"form": form})
        else:
            return redirect("accounts:login")

    else:
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("products:index")