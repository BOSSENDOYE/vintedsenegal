from django.db import models
from django.conf import settings
from listings.models import Listing

class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reviews')
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name='reviews')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.user} on {self.listing}"

class Rating(models.Model):
    review = models.OneToOneField(Review, on_delete=models.CASCADE, related_name='rating')
    score = models.PositiveSmallIntegerField()

    def __str__(self):
        return f"Rating {self.score} for review {self.review.id}"
