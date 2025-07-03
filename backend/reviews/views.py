from rest_framework import generics, permissions
from .models import Review, Rating
from .serializers import ReviewSerializer, RatingSerializer

class ReviewListCreateView(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        print('Données reçues pour création review:', request.data)
        return super().create(request, *args, **kwargs)

class RatingListCreateView(generics.ListCreateAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        print('Données reçues pour création rating:', request.data)
        return super().create(request, *args, **kwargs)
