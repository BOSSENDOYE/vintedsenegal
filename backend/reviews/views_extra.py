from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class ReviewsHomeView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({
            "message": "Bienvenue au système d'évaluation VintedDD.",
            "endpoints": {
                "reviews": "/api/reviews/",
                "review_detail": "/api/reviews/{id}/",
            }
        })
