from django.shortcuts import render, redirect
from posts.models import Post
from .forms import CreateUserForm, LoginForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout


def register(request):
    if request.method == "GET":
        form = CreateUserForm()
        return render(request, "register.html", context={"registerform": form})

    if request.method == "POST":
        form = CreateUserForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            login(request, user)
            return redirect("index")
        else:
            return render(
                request, "register.html", context={"registerform": form}, status=400
            )


def login_user(request):
    if request.method == "GET":
        form = LoginForm()
        return render(request, "login.html", context={"loginform": form})

    if request.method == "POST":
        form = LoginForm(request, data=request.POST)

        if form.is_valid():
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect("index")

    return render(request, "login.html", context={"loginform": form}, status=400)


@login_required(login_url="login")
def user_logout(request):
    logout(request)
    return redirect("index")


@login_required(login_url="login")
def profile(request):
    posts = Post.objects.filter(author=request.user)
    return render(request, "profile.html", context={"posts": posts})
