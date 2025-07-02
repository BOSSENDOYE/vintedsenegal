from django.urls import path
from .views import ReviewListCreateView, RatingListCreateView
from .views_extra import ReviewsHomeView

urlpatterns = [
    path('', ReviewsHomeView.as_view(), name='reviews-home'),
    path('reviews/', ReviewListCreateView.as_view(), name='review-list-create'),
    path('ratings/', RatingListCreateView.as_view(), name='rating-list-create'),
]
