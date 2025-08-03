from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from django.views.generic.detail import DetailView

from .models import Book
from .models import Library
from .models import Author
from .models import Librarian
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

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


class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'relationship_app/register.html'
    success_url = reverse_lazy('relationship_app:login')







