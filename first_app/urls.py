
from django.urls import path, include
from .import views
urlpatterns = [

     path('register/', views.Register, name='register'),
     path('login/', views.user_login, name='user_login'),
     path('profile/', views.user_profile, name='user_profile'),
     path('change_password/', views.change_password, name='change_password'),
     path('change_without_old_password/', views.pass_changeWithoutOldPass, name='change_without_old_password'),
     path('profile/', views.user_profile, name='user_profile'),
     path('logout/', views.user_logout, name='user_logout'),

    
]