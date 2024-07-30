from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Category, Book, Author
from .serializers import CategorySerializer, BookSerializer, AuthorSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all().select_related('category').prefetch_related('author')
    serializer_class = BookSerializer

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.prefetch_related('books__category').all()
    serializer_class = AuthorSerializer
