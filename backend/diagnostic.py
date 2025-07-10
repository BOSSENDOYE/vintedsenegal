#!/usr/bin/env python3
"""
Script de diagnostic pour identifier les problèmes
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
from listings.models import Category, Listing
import json

User = get_user_model()

def check_database():
    """Vérifier la base de données"""
    print("🔍 Diagnostic de la base de données")
    print("=" * 50)
    
    # Vérifier les utilisateurs
    users = User.objects.all()
    print(f"👥 Utilisateurs: {users.count()}")
    for user in users:
        print(f"   - {user.username} (ID: {user.id})")
    
    # Vérifier les catégories
    categories = Category.objects.all()
    print(f"\n🏷️ Catégories: {categories.count()}")
    for cat in categories:
        print(f"   - {cat.name} (ID: {cat.id})")
    
    # Vérifier les annonces
    listings = Listing.objects.all()
    print(f"\n📋 Annonces: {listings.count()}")
    for listing in listings:
        print(f"   - {listing.title} (ID: {listing.id}, Vendeur: {listing.seller.username if listing.seller else 'Aucun'})")

def test_api_endpoints():
    """Tester les endpoints API"""
    print("\n🌐 Test des endpoints API")
    print("=" * 50)
    
    client = Client()
    
    # Test de l'endpoint de connexion
    print("\n1️⃣ Test de connexion...")
    login_data = {
        'username': 'testuser',
        'password': 'testpass123'
    }
    
    response = client.post('/api/users/login/', 
                          data=json.dumps(login_data),
                          content_type='application/json')
    
    print(f"   Status: {response.status_code}")
    if response.status_code == 200:
        data = json.loads(response.content)
        print(f"   ✅ Connexion réussie")
        access_token = data.get('access')
        
        # Test de création d'annonce
        print("\n2️⃣ Test de création d'annonce...")
        listing_data = {
            'title': 'Test Diagnostic',
            'description': 'Test de diagnostic',
            'price': '10000',
            'category': 'Femmes'
        }
        
        headers = {
            'HTTP_AUTHORIZATION': f'Bearer {access_token}',
            'content_type': 'application/json'
        }
        
        create_response = client.post('/api/listings/create/',
                                     data=json.dumps(listing_data),
                                     **headers)
        
        print(f"   Status: {create_response.status_code}")
        print(f"   Response: {create_response.content.decode()}")
        
        if create_response.status_code == 201:
            print("   ✅ Création réussie")
        else:
            print("   ❌ Échec de création")
    else:
        print(f"   ❌ Échec de connexion: {response.content.decode()}")
    
    # Test de récupération des annonces
    print("\n3️⃣ Test de récupération des annonces...")
    list_response = client.get('/api/listings/')
    print(f"   Status: {list_response.status_code}")
    if list_response.status_code == 200:
        data = json.loads(list_response.content)
        print(f"   ✅ {len(data)} annonces trouvées")
    else:
        print(f"   ❌ Échec: {list_response.content.decode()}")

def check_settings():
    """Vérifier les paramètres"""
    print("\n⚙️ Vérification des paramètres")
    print("=" * 50)
    
    print(f"DEBUG: {settings.DEBUG}")
    print(f"CORS_ALLOW_ALL_ORIGINS: {getattr(settings, 'CORS_ALLOW_ALL_ORIGINS', 'Non défini')}")
    print(f"ALLOWED_HOSTS: {settings.ALLOWED_HOSTS}")
    print(f"INSTALLED_APPS: {len(settings.INSTALLED_APPS)} apps")
    
    # Vérifier les middlewares
    print(f"\nMiddlewares:")
    for middleware in settings.MIDDLEWARE:
        print(f"   - {middleware}")

def create_test_data():
    """Créer des données de test"""
    print("\n🔧 Création de données de test")
    print("=" * 50)
    
    # Créer un utilisateur de test
    user, created = User.objects.get_or_create(
        username='testuser',
        defaults={'email': 'test@example.com'}
    )
    if created:
        user.set_password('testpass123')
        user.save()
        print("✅ Utilisateur de test créé")
    else:
        print("ℹ️ Utilisateur de test existant")
    
    # Créer une catégorie de test
    category, created = Category.objects.get_or_create(name='Femmes')
    if created:
        print("✅ Catégorie 'Femmes' créée")
    else:
        print("ℹ️ Catégorie 'Femmes' existante")

if __name__ == '__main__':
    create_test_data()
    check_database()
    check_settings()
    test_api_endpoints()
    
    print("\n🎯 Résumé du diagnostic:")
    print("=" * 50)
    print("1. Vérifiez que l'utilisateur 'testuser' existe")
    print("2. Vérifiez que la catégorie 'Femmes' existe")
    print("3. Vérifiez que le serveur Django fonctionne sur le port 8000")
    print("4. Vérifiez que le frontend fonctionne sur le port 3000")
    print("5. Vérifiez les logs du serveur Django pour les erreurs détaillées") 