from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import NewUserForm
from .models import Post


#  view function for home page
def home(request):
    # Getting object of database
    posts = Post.objects.all()
    return render(request, "crmapp/home.html", {"posts": posts})


# view for register page
def register_user(request):
    # Check if the method is post
    if request.method == "POST":
        form = NewUserForm(request.POST)

        # Check if the form is valid
        if form.is_valid():
            form.save()

            # authenticate & login
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            user = authenticate(request, username=username, password=password)

            # double check if user registered succesfully
            if user is not None:
                login(request, user)
                messages.success(request, "You have been registered successfully")
                return redirect("home")
    else:
        form = NewUserForm()
        return render(request, "crmapp/register.html", {"form": form})
    return render(request, "crmapp/register.html", {"form": form})


# view for login page
def login_user(request):
    # Check if the request method is post
    if request.method == "POST":
        uname = request.POST.get("username")
        pswd = request.POST.get("password")

        # authenticating user
        user = authenticate(request, username=uname, password=pswd)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged in successfully...")
            return redirect("home")
        else:
            messages.warning(request, "couldn't log in ...")
    return render(request, "crmapp/login.html")


# view for logging out
def logout_user(request):
    logout(request)
    messages.success(request, "You have been successfully logged out...")
    return redirect("home")


# view for individual post
def individual_post(request, pk):
    # Check if the user is logged in
    if request.user.is_authenticated:
        user_post = Post.objects.get(id=pk)
        return render(request, "crmapp/post.html", {"user_post": user_post})
    else:
        messages.warning(request, "You need to log in ")
        return redirect("login")


#  view for deleting a post
def delete_post(request, pk):
    # checking is the user is a valid user
    if request.user.is_authenticated:

        # creating object for that post
        post = Post.objects.get(id=pk)

        # User can only delete the post if he posted that post
        if request.user.email == post.email:
            post.delete()
            messages.success(request, "Post deleted successfully")
            return redirect("home")
        else:
            messages.warning(request,"You are signed in as "+request.user.email+" So you can't delete this post")
            return redirect("home")

    else:
        messages.warning(request, "You need to login first")
        return redirect("login")

    return render(request, "crmapp/home.html")


# View for adding new post

def add_post(request):

    # Checking if the user is logged in
    if request.user.is_authenticated:

        # checking if the request is post
        if request.method == "POST":

            # getting variables from form
            username = request.POST.get("username")
            email = request.POST.get("email")
            caption = request.POST.get("caption")
            content = request.POST.get("content")

            # Adding variables to Database
            new_post = Post()
            new_post.user_name = username
            new_post.email = email
            new_post.caption = caption
            new_post.content = content
            new_post.save()

            return redirect("home")
    else:
        messages.warning(request,"You need to login to add a post...")
        return redirect("login")
    return render(request, "crmapp/add_post.html")


# Views for updating post

def update_post(request, pk):

    # Checking if the user is authenticated
    if request.user.is_authenticated:

        # fetching current data
        current_post = Post.objects.get(id=pk)

        if request.method == "POST":
            # getting variables from form
            username = request.POST.get("username")
            email = request.POST.get("email")
            caption = request.POST.get("caption")
            content = request.POST.get("content")

            # updating variables to Database
            current_post.user_name = username
            current_post.email = email
            current_post.caption = caption
            current_post.content = content
            current_post.save()

            return redirect("home")
    else:
        messages.warning(request, "You need to login to add a post...")
        return redirect("login")
    return render(request, "crmapp/update_post.html",{"current_post":current_post})

