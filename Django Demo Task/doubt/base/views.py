from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib import messages
from .models import Youtube, Posts, Userprofile
from django.contrib.sessions.models import Session
from django.contrib.auth.forms import UserCreationForm
from math import ceil
# Create your views here.


def home(request):
    phy = Youtube.objects.all()
    phy = Youtube.objects.filter().order_by('-time_stamp')[:3]
    post = Posts.objects.all()
    post = Posts.objects.filter().order_by('-time_stamp')[:3]
    context = {'phy': phy, 'post': post}

    return render(request, 'home.html', context)


def lectures(request):
    phy = Youtube.objects.all()
    context = {'phy': phy, }
    return render(request, 'lecture.html', context)


def handleSignup(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if len(username) > 10:
            messages.error(
                request, "username should be less than 10 characters")
            return redirect("home")

        if not username.isalnum():

            messages.error(request, "username should be alphanumeric")
            return redirect("home")
        for c in username:
            if c.isupper():

                messages.error(request, "username should be in lower case")
                return redirect("home")
                break

        if pass1 != pass2:
            messages.error(request, "Passwords dit not match")
            return redirect("home")

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = first_name
        myuser.last_name = last_name
        myuser.save()
        # Userprofile.objects.get(user=request.user,)

        messages.success(
            request, "Your Coursify account has been created successfully.")
        return redirect("home")
    else:
        return HttpResponse("404 - Not Found")


def handleLogin(request):
    if request.method == 'POST':
        loginusername = request.POST['lusername']
        loginpassword = request.POST['pass']

        user = authenticate(username=loginusername, password=loginpassword)

        if user is not None:
            login(request, user)
            messages.success(request, "Succesfully logged in")
            request.session['is_logged'] = True

            return redirect("home")
        else:
            messages.error(request, "Invalid credentials, Please try again")
            return redirect("home")
    else:
        return HttpResponse("404 - Not Found")


def handleLogout(request):
    # del request.session['is_logged']
    logout(request)

    messages.success(request, "Succesfully logged out")
    return redirect('home')


# def profile(request):

#     user_profile = Userprofile.objects.get(user__id=request.user.id)

#     context = {'user_profile': user_profile}

#     return render(request, 'profile.html', context)


def search(request):
    query = request.GET['search']

    if len(query) > 78 or len(query) < 1:
        allPosts = Posts.objects.none()
        messages.error(request, "invalid query")
    # return render(request, 'search.html')
    else:
        allPostsTitle = Posts.objects.filter(title__icontains=query)
        allPostsContent = Posts.objects.filter(content__icontains=query)
        allPosts = allPostsTitle.union(allPostsContent)

    if allPosts.count() == 0:
        messages.warning(request, "OOPS! No result found.")
    params = {'allPosts': allPosts, 'query': query}
    return render(request, 'search.html', params)
