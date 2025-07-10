#!/usr/bin/env python3
"""
Script pour créer un utilisateur de test et tester l'authentification
"""

import os
import sys
import django
from django.conf import settings

# Configuration Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

from django.contrib.auth import get_user_model
from django.test import Client
import json

User = get_user_model()

def create_test_user():
    """Créer un utilisateur de test"""
    print("👤 Création d'un utilisateur de test")
    print("=" * 50)
    
    # Supprimer l'utilisateur s'il existe
    try:
        user = User.objects.get(username='testuser')
        user.delete()
        print("Utilisateur test existant supprimé")
    except User.DoesNotExist:
        pass
    
    # Créer un nouvel utilisateur
    user = User.objects.create_user(
        username='testuser',
        email='test@example.com',
        password='testpass123'
    )
    print(f"✅ Utilisateur créé: {user.username} (ID: {user.id})")
    print(f"   Email: {user.email}")
    print(f"   Password: testpass123")
    return user

def test_login():
    """Tester la connexion"""
    print("\n🧪 Test de connexion")
    print("=" * 50)
    
    client = Client()
    
    # Test avec des identifiants valides
    login_data = {
        'username': 'testuser',
        'password': 'testpass123'
    }
    
    print("Tentative de connexion avec:")
    print(f"   Username: {login_data['username']}")
    print(f"   Password: {login_data['password']}")
    
    response = client.post('/api/users/login/', 
                          data=json.dumps(login_data),
                          content_type='application/json')
    
    print(f"\nStatus Code: {response.status_code}")
    print(f"Response: {response.content.decode()}")
    
    if response.status_code == 200:
        data = json.loads(response.content)
        print("\n✅ Connexion réussie!")
        print(f"Access Token: {data.get('access', 'Non trouvé')[:50]}...")
        print(f"Refresh Token: {data.get('refresh', 'Non trouvé')[:50]}...")
        return data.get('access')
    else:
        print("\n❌ Échec de la connexion")
        return None

def test_manual_auth():
    """Test d'authentification manuelle"""
    print("\n🔍 Test d'authentification manuelle")
    print("=" * 50)
    
    from django.contrib.auth import authenticate
    from users.views import UsernameOrEmailBackend
    
    backend = UsernameOrEmailBackend()
    
    # Test avec username
    user = backend.authenticate(None, username='testuser', password='testpass123')
    if user:
        print(f"✅ Authentification réussie avec username: {user.username}")
    else:
        print("❌ Échec d'authentification avec username")
    
    # Test avec email
    user = backend.authenticate(None, username='test@example.com', password='testpass123')
    if user:
        print(f"✅ Authentification réussie avec email: {user.username}")
    else:
        print("❌ Échec d'authentification avec email")

def list_users():
    """Lister tous les utilisateurs"""
    print("\n📋 Liste des utilisateurs")
    print("=" * 50)
    
    users = User.objects.all()
    if users:
        for user in users:
            print(f"   {user.username} ({user.email}) - ID: {user.id}")
    else:
        print("   Aucun utilisateur trouvé")

if __name__ == '__main__':
    list_users()
    user = create_test_user()
    test_manual_auth()
    access_token = test_login()
    
    if access_token:
        print("\n🎉 Test complet réussi!")
    else:
        print("\n❌ Il y a encore un problème avec l'authentification") 