#!/usr/bin/env python3
"""
Test de création d'annonce
"""

import os
import sys
import django
from django.conf import settings

# Configuration Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

from django.test import Client
from django.contrib.auth import get_user_model
import json

User = get_user_model()

def test_listing_creation():
    """Test de création d'annonce"""
    print("🧪 Test de création d'annonce")
    print("=" * 50)
    
    client = Client()
    
    # 1. Se connecter
    print("\n1️⃣ Connexion...")
    login_response = client.post('/api/users/login/', 
                                data=json.dumps({
                                    'username': 'testuser',
                                    'password': 'testpass123'
                                }),
                                content_type='application/json')
    
    if login_response.status_code != 200:
        print(f"❌ Échec de connexion: {login_response.status_code}")
        return False
    
    login_data = json.loads(login_response.content)
    access_token = login_data.get('access')
    print(f"✅ Connexion réussie, token: {access_token[:50]}...")
    
    # 2. Créer une annonce
    print("\n2️⃣ Création d'annonce...")
    listing_data = {
        'title': 'Test Annonce',
        'description': 'Description de test pour vérifier la création',
        'price': '15000',
        'category': 'Femmes'
    }
    
    headers = {
        'HTTP_AUTHORIZATION': f'Bearer {access_token}',
        'content_type': 'application/json'
    }
    
    create_response = client.post('/api/listings/create/',
                                 data=json.dumps(listing_data),
                                 **headers)
    
    print(f"Status: {create_response.status_code}")
    print(f"Response: {create_response.content.decode()}")
    
    if create_response.status_code == 201:
        print("✅ Création d'annonce réussie!")
        return True
    else:
        print("❌ Échec de création d'annonce")
        return False

def test_listing_list():
    """Test de récupération des annonces"""
    print("\n3️⃣ Test de récupération des annonces...")
    
    client = Client()
    response = client.get('/api/listings/')
    
    print(f"Status: {response.status_code}")
    if response.status_code == 200:
        data = json.loads(response.content)
        print(f"✅ {len(data)} annonces trouvées")
        return True
    else:
        print("❌ Échec de récupération des annonces")
        return False

if __name__ == '__main__':
    success1 = test_listing_creation()
    success2 = test_listing_list()
    
    if success1 and success2:
        print("\n🎉 Tous les tests sont passés!")
    else:
        print("\n❌ Certains tests ont échoué") 