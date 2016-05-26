from django.db import models
from django.forms import ModelForm


class Editor(models.Model):
    name = models.CharField(max_length=256, default=" ")

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=256, default=" ")

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=256, default=" ")

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=256, default=" xxx ")
    editor = models.ForeignKey(Editor)
    category = models.ForeignKey(Category)
    author = models.ForeignKey(Author)


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['name',  'editor', 'category', 'author']
