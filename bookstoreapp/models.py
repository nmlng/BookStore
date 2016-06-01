from django.db import models
from django.forms import ModelForm


class Editor(models.Model):
    name = models.CharField(max_length=256, default="")

    def __str__(self):
        return self.name


class EditorForm(ModelForm):
    class Meta:
        model = Editor
        fields = ['name']


class Author(models.Model):
    name = models.CharField(max_length=256, default="")

    def __str__(self):
        return self.name


class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = ['name']


class Category(models.Model):
    name = models.CharField(max_length=256, default="")

    def __str__(self):
        return self.name


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['name']


class Book(models.Model):
    name = models.CharField(max_length=256, default="")
    editor = models.ForeignKey(Editor)
    category = models.ForeignKey(Category)
    author = models.ForeignKey(Author)


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['category', 'name', 'author', 'editor']
