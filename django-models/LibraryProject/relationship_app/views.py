from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.views.generic import DetailView

from .models import Book, Library, Author, Librarian

# Create your views here.

def index(request):
    return HttpResponse("Welcome To The Home Page!")


def list_books(request):
    books = Book.objects.all()
    #authors = books.author_set
    context = {'books':books}
    return render(request,'relationship_app/list_books.html',context)

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

    print(context_object_name)





