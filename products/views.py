from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404

from django.views.decorators.http import require_http_methods, require_POST
from django.contrib.auth.decorators import login_required

from .models import Post, Comment
from .forms import PostForm, CommentForm
# Create your views here.


def index(request):
    # form = PostForm()
    posts = Post.objects.all()

    context = {
        # "form": form,
        "posts": posts,
    }
    return render(request, "products/index.html", context)


@login_required()
@require_http_methods(["GET", "POST"])
def create(request):
    if request.method == "GET":
        form = PostForm()
        return render(request, "products/create.html", {"form": form})

    else:
        # files = request.FILES # 넘어온 파일
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect("products:detail", post.pk)


def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comment_form = CommentForm()
    comments = post.comments.all().order_by("-created_time")

    context = {
        "post": post,
        "comments": comments,
        "comment_form": comment_form,
    }
    return render(request, "products/detail.html", context)


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
                   "post": post,
                   }
        return render(request, "products/update.html", context)


@require_POST
def delete(request, pk):
    # if request.user.is_authenticated:
    post = get_object_or_404(Post, pk=pk)

    if post.author == request.user:
        post.delete()
    return redirect("products:index")



@login_required()
@require_POST
def comment(request, pk):
    post = get_object_or_404(Post, pk=pk)
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.save()
        return redirect("products:detail", pk)


@login_required()
@require_POST
def comment_delete(request, post_pk, comment_pk):
    post = get_object_or_404(Post, pk=post_pk)
    comment = Comment.objects.get(post=post, pk=comment_pk)
    comment.delete()
    return redirect("products:detail", post_pk)


def like(request, pk):
    post = get_object_or_404(Post, pk=pk)
    