#!/usr/bin/env python3
"""
Test rapide de l'authentification
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

def quick_test():
    """Test rapide"""
    print("🚀 Test rapide de l'authentification")
    print("=" * 40)
    
    # Créer un utilisateur
    user, created = User.objects.get_or_create(
        username='testuser',
        defaults={'email': 'test@example.com'}
    )
    if created:
        user.set_password('testpass123')
        user.save()
        print("✅ Utilisateur créé")
    else:
        user.set_password('testpass123')
        user.save()
        print("✅ Utilisateur mis à jour")
    
    # Tester la connexion
    client = Client()
    response = client.post('/api/users/login/', 
                          data=json.dumps({
                              'username': 'testuser',
                              'password': 'testpass123'
                          }),
                          content_type='application/json')
    
    print(f"Status: {response.status_code}")
    print(f"Response: {response.content.decode()}")
    
    if response.status_code == 200:
        print("🎉 SUCCÈS ! L'authentification fonctionne !")
        return True
    else:
        print("❌ ÉCHEC ! L'authentification ne fonctionne pas.")
        return False

if __name__ == '__main__':
    quick_test() 