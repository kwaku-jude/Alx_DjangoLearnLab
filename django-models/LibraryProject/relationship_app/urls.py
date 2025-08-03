from django.urls import path
from . import views
from .views import list_books

app_name = 'relationship_app'

urlpatterns = [
    path('',views.index,name='index'),
    path('list_books',views.list_books,name='list_books'),
    path('library_detail/<int:pk>/',views.LibraryDetailView.as_view(),name='library_detail'),
]