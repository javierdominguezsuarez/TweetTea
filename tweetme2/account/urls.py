from rest_framework import viewsets
from .views import ProfileAPI, RegisterAPI
from django.urls import path
from knox import views as knox_views
from .views import LoginAPI
urlpatterns = [
    path('register/', RegisterAPI.as_view(), name='register'),
    path('login/', LoginAPI.as_view(), name='login'),
    path('logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
    #path('<str:username>',profile_detail_view),
    path('profile/<int:user_id>',ProfileAPI.as_view(),name= 'profile')
]