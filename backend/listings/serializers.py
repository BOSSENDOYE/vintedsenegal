from rest_framework import serializers
from .models import Listing, Category, Photo

class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ['id', 'image']

class ListingSerializer(serializers.ModelSerializer):
    photos = PhotoSerializer(many=True, read_only=True)
    category = serializers.StringRelatedField()

    class Meta:
        model = Listing
        fields = ['id', 'title', 'description', 'category', 'price', 'created_at', 'photos']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']
