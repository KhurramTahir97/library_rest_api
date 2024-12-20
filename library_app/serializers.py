from rest_framework import serializers
from .models import Book, Publisher, Author

class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = '__all__'

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    publisher = PublisherSerializer()
    authors = AuthorSerializer(many=True)

    class Meta:
        model = Book
        fields = '__all__'