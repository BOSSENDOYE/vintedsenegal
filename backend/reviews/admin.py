from django.contrib import admin
from .models import Review, Rating

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'listing', 'content', 'created_at')
    search_fields = ('content', 'user__username')

@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('id', 'review', 'score')
