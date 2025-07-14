from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions, generics
from django.contrib.auth import get_user_model
from .models import Message, Conversation
from .serializers import MessageSerializer, ConversationSerializer, SendMessageSerializer

User = get_user_model()

class MessageCreateView(generics.CreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        print('Données reçues pour création message:', request.data)
        return super().create(request, *args, **kwargs)

class ConversationListView(generics.ListAPIView):
    serializer_class = ConversationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Conversation.objects.filter(participants=user)

class ConversationDetailView(generics.RetrieveAPIView):
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer
    permission_classes = [permissions.IsAuthenticated]

class SendMessageToUserView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        serializer = SendMessageSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        recipient_id = serializer.validated_data['recipient_id']
        content = serializer.validated_data['content']
        subject = serializer.validated_data.get('subject', '')

        try:
            recipient = User.objects.get(pk=recipient_id)
        except User.DoesNotExist:
            return Response({'error': 'Utilisateur destinataire introuvable.'}, status=404)

        # Chercher une conversation existante entre les deux utilisateurs
        conversation = Conversation.objects.filter(participants=request.user).filter(participants=recipient).first()
        if not conversation:
            conversation = Conversation.objects.create(subject=subject or f"Conversation avec {recipient.username}")
            conversation.participants.add(request.user, recipient)

        # Créer le message
        message = Message.objects.create(
            conversation=conversation,
            sender=request.user,
            content=content
        )

        return Response(MessageSerializer(message).data, status=201)
