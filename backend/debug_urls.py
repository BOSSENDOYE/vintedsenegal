#!/usr/bin/env python3
"""
Script de débogage des URLs
"""

import os
import sys
import django
from django.conf import settings

# Configuration Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

from django.urls import get_resolver
from django.test import Client
import json

def debug_urls():
    """Déboguer les URLs disponibles"""
    print("🔍 Débogage des URLs Django")
    print("=" * 50)
    
    # Obtenir le resolver d'URLs
    resolver = get_resolver()
    
    print("URLs disponibles:")
    for pattern in resolver.url_patterns:
        print(f"  {pattern.pattern}")
        if hasattr(pattern, 'url_patterns'):
            for sub_pattern in pattern.url_patterns:
                print(f"    {sub_pattern.pattern} -> {sub_pattern.callback.__name__ if hasattr(sub_pattern, 'callback') else 'N/A'}")

def test_api_endpoints():
    """Tester les endpoints API"""
    print("\n🧪 Test des endpoints API")
    print("=" * 50)
    
    client = Client()
    
    # Test de l'endpoint racine de l'API
    print("1. Test de l'endpoint racine /api/")
    response = client.get('/api/')
    print(f"   Status: {response.status_code}")
    print(f"   Content: {response.content.decode()[:100]}...")
    
    # Test de l'endpoint de connexion
    print("\n2. Test de l'endpoint de connexion /api/users/login/")
    login_data = {
        'username': 'testuser',
        'password': 'testpass123'
    }
    response = client.post('/api/users/login/', 
                          data=json.dumps(login_data),
                          content_type='application/json')
    print(f"   Status: {response.status_code}")
    print(f"   Content: {response.content.decode()[:200]}...")
    
    # Test de l'endpoint d'inscription
    print("\n3. Test de l'endpoint d'inscription /api/users/register/")
    register_data = {
        'username': 'newuser',
        'email': 'new@example.com',
        'password': 'newpass123'
    }
    response = client.post('/api/users/register/', 
                          data=json.dumps(register_data),
                          content_type='application/json')
    print(f"   Status: {response.status_code}")
    print(f"   Content: {response.content.decode()[:200]}...")

def test_direct_view():
    """Tester directement la vue de connexion"""
    print("\n🎯 Test direct de la vue de connexion")
    print("=" * 50)
    
    from users.views import LoginView
    from django.test import RequestFactory
    from django.contrib.auth import get_user_model
    
    User = get_user_model()
    
    # Créer un utilisateur de test
    user, created = User.objects.get_or_create(
        username='testuser',
        defaults={'email': 'test@example.com'}
    )
    if created:
        user.set_password('testpass123')
        user.save()
        print("Utilisateur de test créé")
    else:
        print("Utilisateur de test existe déjà")
    
    # Créer une requête de test
    factory = RequestFactory()
    request = factory.post('/api/users/login/', 
                          data=json.dumps({
                              'username': 'testuser',
                              'password': 'testpass123'
                          }),
                          content_type='application/json')
    
    # Appeler la vue directement
    view = LoginView()
    response = view.post(request)
    
    print(f"Status: {response.status_code}")
    print(f"Content: {response.content.decode()[:200]}...")

if __name__ == '__main__':
    debug_urls()
    test_api_endpoints()
    test_direct_view() 