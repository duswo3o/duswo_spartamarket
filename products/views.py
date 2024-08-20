from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404

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


def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, "products/detail.html", {"post":post})


@require_http_methods(["GET", "POST"])
def update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect("products:detail", pk)
    else:
        form = PostForm(instance=post)
        context = {"form": form,
                   "post": post
                   }
        return render(request, "products/update.html", context)


@require_POST
def delete(request, pk):
    # if request.user.is_authenticated:
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect("products:index")