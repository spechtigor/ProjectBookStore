from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.viewsets import ModelViewSet

from Store.models import Book
from Store.serializers import BooksSerializer, AuthorsSerializer


# Create your views here.
class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BooksSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filter_fields = ['title', 'description']
    search_fields = ['title', 'author_id']
    ordering_fields = ['title', 'author_id']


class AuthorViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = AuthorsSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filter_fields = ['name']
    search_fields = ['name']
    ordering_fields = ['name']
