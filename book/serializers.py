from rest_framework import serializers
from .models import Category, Book, Author

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), required=False, allow_null=True)

    class Meta:
        model = Book
        fields = '__all__'

    def create(self, validated_data):
        category = validated_data.pop('category', None)
        book = Book.objects.create(category=category, **validated_data)
        return book

class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, required=False)

    class Meta:
        model = Author
        fields = '__all__'

    def create(self, validated_data):
        books_data = validated_data.pop('books', [])
        author = Author.objects.create(**validated_data)
        for book_data in books_data:
            Book.objects.create(author=author, **book_data)
        return author