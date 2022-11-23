from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=255, blank=False)
    description = models.CharField(max_length=255)
    author = models.ForeignKey('Author', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title


class Author(models.Model):
    name = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return self.name
