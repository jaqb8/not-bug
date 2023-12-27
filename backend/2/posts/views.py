from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from posts.forms import CreatePostForm
from posts.models import Post


def index(request):
    posts = Post.objects.all()
    context = {
        "posts": posts,
    }
    if request.user.is_authenticated:
        form = CreatePostForm()
        context["create_post_form"] = form

    return render(request, "index.html", context=context)


@login_required(login_url="login")
def create_post(request):
    if request.method == "POST":
        form = CreatePostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect(
                "index",
            )
        else:
            return render(
                request,
                "index.html",
                context={"create_post_form": form},
                status=400,
            )


def post_detail(request, id):
    post = Post.objects.get(pk=id)
    return render(
        request,
        "post_detail.html",
        context={
            "post": post,
            "can_edit": post.author == request.user,
        },
    )


@login_required(login_url="login")
def post_edit(request, id):
    post = Post.objects.get(pk=id)

    if post.author != request.user:
        return redirect(
            "post-detail",
            id=id,
        )

    if request.method == "POST":
        form = CreatePostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect(
                "post-detail",
                id=id,
            )
        else:
            return render(
                request,
                "post_edit.html",
                context={
                    "edit_post_form": form,
                    "post": post,
                },
                status=400,
            )
    else:
        form = CreatePostForm(instance=post)
        return render(
            request,
            "post_edit.html",
            context={
                "edit_post_form": form,
                "post": post,
            },
        )
