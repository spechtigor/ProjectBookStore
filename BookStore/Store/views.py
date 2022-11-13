from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from Store.models import Book
from Store.serializers import BooksSerializer, AuthorsSerializer


# Create your views here.
class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BooksSerializer


class AuthorViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = AuthorsSerializer
