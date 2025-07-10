#!/usr/bin/env python3
"""
Script de test pour diagnostiquer les problèmes d'authentification
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

def test_user_creation():
    """Test de création d'utilisateur"""
    print("=== Test de création d'utilisateur ===")
    
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
    print(f"Utilisateur créé: {user.username} (ID: {user.id})")
    return user

def test_login_api():
    """Test de l'API de connexion"""
    print("\n=== Test de l'API de connexion ===")
    
    client = Client()
    
    # Test avec des identifiants valides
    login_data = {
        'username': 'testuser',
        'password': 'testpass123'
    }
    
    response = client.post('/api/users/login/', 
                          data=json.dumps(login_data),
                          content_type='application/json')
    
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.content.decode()}")
    
    if response.status_code == 200:
        data = json.loads(response.content)
        print("✅ Connexion réussie!")
        print(f"Access Token: {data.get('access', 'Non trouvé')[:50]}...")
        print(f"Refresh Token: {data.get('refresh', 'Non trouvé')[:50]}...")
        return data.get('access')
    else:
        print("❌ Échec de la connexion")
        return None

def test_protected_endpoint(access_token):
    """Test d'un endpoint protégé"""
    print("\n=== Test d'endpoint protégé ===")
    
    client = Client()
    
    headers = {
        'HTTP_AUTHORIZATION': f'Bearer {access_token}',
        'content_type': 'application/json'
    }
    
    response = client.get('/api/users/profile/', **headers)
    
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.content.decode()}")
    
    if response.status_code == 200:
        print("✅ Accès à l'endpoint protégé réussi!")
    else:
        print("❌ Échec d'accès à l'endpoint protégé")

def main():
    """Fonction principale"""
    print("🔍 Diagnostic d'authentification Vinted")
    print("=" * 50)
    
    try:
        # Test 1: Création d'utilisateur
        user = test_user_creation()
        
        # Test 2: Connexion API
        access_token = test_login_api()
        
        # Test 3: Endpoint protégé
        if access_token:
            test_protected_endpoint(access_token)
        
        print("\n✅ Tous les tests terminés!")
        
    except Exception as e:
        print(f"\n❌ Erreur lors des tests: {e}")
        import traceback
        traceback.print_exc()

if __name__ == '__main__':
    main() 