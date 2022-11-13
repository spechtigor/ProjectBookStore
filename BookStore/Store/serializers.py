from rest_framework.serializers import ModelSerializer

from Store.models import Book, Author


class BooksSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class AuthorsSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'