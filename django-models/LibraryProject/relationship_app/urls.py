from django.contrib import auth
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import list_books, SignUpView
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView

app_name = 'relationship_app'

urlpatterns = [
    path('',views.index,name='index'),
    path('list_books',views.list_books,name='list_books'),
    path('library_detail/<int:pk>/',views.LibraryDetailView.as_view(),name='library_detail'),

    #authentication views
    #login
    path('login/', auth_views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/',SignUpView.as_view(),name='register'),
    path('admin/logout/', auth_views.LogoutView.as_view(next_page='relationship_app/logout.html'), name='logout')
]