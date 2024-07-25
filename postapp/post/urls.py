from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('<int:post_id>/edit/', views.post_edit, name='post_edit'),
    path('<int:post_id>/delete/', views.post_delete, name='post_delete'),
    path('create/', views.post_create, name='post_create'),
    path('register/', views.register, name='register'),
    path('profile_form/', views.profile_form, name='profile_form'),
    path('profile_view/', views.profile_view, name='profile'),
]