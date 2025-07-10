from rest_framework import serializers
from .models import Listing, Category, Photo

class PhotoSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()
    
    class Meta:
        model = Photo
        fields = ['id', 'image', 'image_url']
    
    def get_image_url(self, obj):
        if obj.image:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.image.url)
            return obj.image.url
        return None

class ListingSerializer(serializers.ModelSerializer):
    photos = PhotoSerializer(many=True, read_only=True)
    category = serializers.StringRelatedField()
    seller = serializers.StringRelatedField()

    class Meta:
        model = Listing
        fields = ['id', 'title', 'description', 'category', 'price', 'seller', 'created_at', 'photos']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']
