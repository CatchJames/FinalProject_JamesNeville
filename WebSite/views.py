from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required, permission_required
from .models import MovieReview
from .forms import MovieReviewForm
import requests


@login_required(login_url='welcome')
def home(request):
    #reviews = MovieReview.objects.filter(created_by=request.user)
    reviews = MovieReview.objects.all()
    data = MovieReview.objects.all()
    context = {'data': data, 'reviews': reviews}

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
            return redirect('explore')

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
def add_review(request, id):
    last_record = MovieReview.objects.get(id=id)
    form = MovieReviewForm(request.POST or None, instance=last_record)
    if request.method == 'POST':
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect('home')
    context = {"form": form, "record": last_record}

    return render(request, 'WebSite/review.html', context)



def storeinfo(request):
    if request.method == 'POST':
        title = request.POST.get("title")
        image = request.POST.get("image")
        year = request.POST.get("year")
        print(title, image, year)
        MovieReview.objects.create(title=title, poster=image, year=year)
        last_record = MovieReview.objects.all().last()
        return redirect('addreview', last_record.id)
    else:
        return redirect('home')


def update_review(request, id):
    review = MovieReview.objects.get(id=id)
    form = MovieReviewForm(request.POST or None, instance=review)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'WebSite/update.html', context)


def delete_review(request, id):
    review = MovieReview.objects.get(id=id)
    context = {'review': review}
    if request.method == 'POST':
        review.delete()
        return redirect('home')

    return render(request, 'Website/delete.html', context)
