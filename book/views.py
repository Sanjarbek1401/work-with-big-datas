from django.shortcuts import render
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
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

    @method_decorator(cache_page(60*15))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.prefetch_related('books__category').all()
    serializer_class = AuthorSerializer
