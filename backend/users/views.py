from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from .serializers import UserSerializer, RegisterSerializer
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()

class UsernameOrEmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(Q(username__iexact=username) | Q(email__iexact=username))
        except User.DoesNotExist:
            return None
        else:
            if user.check_password(password) and self.user_can_authenticate(user):
                return user
        return None

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        print('Données reçues pour inscription:', request.data)
        try:
            response = super().create(request, *args, **kwargs)
            
            # Générer des tokens JWT pour l'utilisateur créé
            user = User.objects.get(username=request.data['username'])
            refresh = RefreshToken.for_user(user)
            
            # Ajouter les tokens à la réponse
            response.data.update({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'message': 'Inscription réussie!'
            })
            
            print(f'Utilisateur créé avec succès: {user.username}')
            return response
            
        except Exception as e:
            print(f'Erreur lors de l\'inscription: {str(e)}')
            return Response({
                'error': f'Erreur lors de l\'inscription: {str(e)}'
            }, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        backend = UsernameOrEmailBackend()
        user = backend.authenticate(request, username=username, password=password)
        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        else:
            return Response({'detail': 'Identifiants invalides.'}, status=status.HTTP_401_UNAUTHORIZED)

class ProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user

class LogoutView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=205)
        except Exception as e:
            return Response(status=400)
