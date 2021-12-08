from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('home/', views.home, name='home'),
    path('addreview/<str:id>', views.add_review, name='addreview'),
    path('updatereview/<int:id>', views.update_review, name='updatereview'),
    path('deletereview/<int:id>', views.delete_review, name='deletereview'),

    path('register/', views.register_user, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),

    path('explore/', views.explore, name='explore'),
    path('storeinfo/', views.storeinfo, name='storeinfo'),


]