from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import CategoryViewSet, BookViewSet, AuthorViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'books', BookViewSet)
router.register(r'authors', AuthorViewSet)

app_name = 'book'

urlpatterns = [
    path('', include(router.urls)),
]
