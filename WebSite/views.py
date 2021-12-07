from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required, permission_required
from .models import MovieReview
from .forms import MovieReviewForm
import requests


@login_required(login_url='welcome')
def homepage(request):
    reviews = MovieReview.objects.filter(user=request.user)
    context = {'reviews': reviews}

    return render(request, 'WebSite/homepage.html', context)


def register_user(request):
    form = UserCreationForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'WebSite/register.html', context)


def login_user(request):
    form = AuthenticationForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')

    context = {'form': form}
    return render(request, 'WebSite/login.html', context)


def logout_user(request):
    logout(request)
    messages.info(request, 'Logout successful')
    return redirect('login')


def welcome(request):
    return render(request, 'WebSite/welcome.html')


def explore(request):
    return render(request, 'WebSite/explore.html')


@login_required(login_url='welcome')
def review(request):
    reviews = MovieReview.objects.all()
    form = MovieReviewForm()
    context = {'form': form, 'reviews': reviews}
    return render(request, 'WebSite/review.html', context)


def add_review(request):
    form = MovieReviewForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect('dune')

    return render(request, 'WebSite/review.html')


def add_movie(request):
    return render(request, 'WebSite/review.html')
