from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class MessagingHomeView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({
            "message": "Bienvenue à la messagerie VintedDD.",
            "endpoints": {
                "conversations": "/api/messaging/conversations/",
                "conversation_detail": "/api/messaging/conversations/{id}/",
                "create_message": "/api/messaging/messages/create/"
            }
        })
