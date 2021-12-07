from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('home/', views.homepage, name='home'),
    path('addreview/', views.add_review, name='addreview'),

    path('register/', views.register_user, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('review/', views.review, name='review'),

    path('explore/', views.explore, name='explore'),

]