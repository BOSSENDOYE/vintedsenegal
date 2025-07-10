#!/usr/bin/env python3
"""
Test simple pour vérifier l'URL de connexion
"""

import os
import sys
import django
from django.conf import settings

# Configuration Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

from django.test import Client
import json

def test_login_url():
    """Test simple de l'URL de connexion"""
    print("🧪 Test simple de l'URL de connexion")
    print("=" * 50)
    
    client = Client()
    
    # Test GET sur l'URL de connexion (pour voir si elle existe)
    print("1. Test GET sur /api/users/login/")
    response = client.get('/api/users/login/')
    print(f"   Status: {response.status_code}")
    print(f"   Content: {response.content.decode()[:100]}...")
    
    # Test POST avec des données JSON
    print("\n2. Test POST sur /api/users/login/")
    login_data = {
        'username': 'testuser',
        'password': 'testpass123'
    }
    
    response = client.post('/api/users/login/', 
                          data=json.dumps(login_data),
                          content_type='application/json')
    print(f"   Status: {response.status_code}")
    print(f"   Content: {response.content.decode()[:200]}...")
    
    # Test avec des données form
    print("\n3. Test POST avec form data")
    response = client.post('/api/users/login/', 
                          data=login_data)
    print(f"   Status: {response.status_code}")
    print(f"   Content: {response.content.decode()[:200]}...")

def test_url_patterns():
    """Vérifier les patterns d'URL"""
    print("\n🔍 Vérification des patterns d'URL")
    print("=" * 50)
    
    from django.urls import reverse
    from django.urls import get_resolver
    
    resolver = get_resolver()
    
    print("URLs disponibles:")
    for pattern in resolver.url_patterns:
        print(f"  {pattern.pattern}")
        if hasattr(pattern, 'url_patterns'):
            for sub_pattern in pattern.url_patterns:
                print(f"    {sub_pattern.pattern}")

if __name__ == '__main__':
    test_url_patterns()
    test_login_url() 