#!/usr/bin/env python3
"""
Test de l'endpoint de détail d'annonce
"""

import os
import sys
import django
from django.conf import settings

# Configuration Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

from django.test import Client
from listings.models import Listing
import json

def test_detail_endpoint():
    """Tester l'endpoint de détail d'annonce"""
    print("🧪 Test de l'endpoint de détail d'annonce")
    print("=" * 50)
    
    client = Client()
    
    # Vérifier qu'il y a des annonces
    listings = Listing.objects.all()
    if not listings.exists():
        print("❌ Aucune annonce trouvée")
        print("💡 Exécutez d'abord: python create_demo_listings.py")
        return
    
    # Prendre la première annonce
    listing = listings.first()
    print(f"📋 Test avec l'annonce: {listing.title} (ID: {listing.id})")
    
    # Tester l'endpoint de détail
    response = client.get(f'/api/listings/{listing.id}/')
    
    print(f"Status: {response.status_code}")
    print(f"URL: /api/listings/{listing.id}/")
    
    if response.status_code == 200:
        data = json.loads(response.content)
        print("✅ Endpoint de détail fonctionne!")
        print(f"   Titre: {data.get('title')}")
        print(f"   Prix: {data.get('price')}")
        print(f"   Catégorie: {data.get('category')}")
        print(f"   Vendeur: {data.get('seller')}")
        print(f"   Photos: {len(data.get('photos', []))}")
        
        # Vérifier les URLs d'images
        photos = data.get('photos', [])
        if photos:
            print(f"   Première image: {photos[0].get('image_url', 'Non trouvée')}")
        else:
            print("   Aucune photo trouvée")
            
    else:
        print(f"❌ Erreur: {response.content.decode()}")
    
    # Tester avec un ID inexistant
    print(f"\n🧪 Test avec ID inexistant...")
    response = client.get('/api/listings/99999/')
    print(f"Status: {response.status_code}")
    
    if response.status_code == 404:
        print("✅ Gestion d'erreur 404 correcte")
    else:
        print(f"❌ Gestion d'erreur incorrecte: {response.status_code}")

def list_all_endpoints():
    """Lister tous les endpoints disponibles"""
    print(f"\n📋 Endpoints disponibles:")
    print("=" * 30)
    
    endpoints = [
        '/api/listings/',
        '/api/listings/categories/',
        '/api/listings/create/',
    ]
    
    client = Client()
    for endpoint in endpoints:
        response = client.get(endpoint)
        print(f"   {endpoint}: {response.status_code}")
    
    # Tester un endpoint de détail spécifique
    listings = Listing.objects.all()
    if listings.exists():
        listing = listings.first()
        endpoint = f'/api/listings/{listing.id}/'
        response = client.get(endpoint)
        print(f"   {endpoint}: {response.status_code}")

if __name__ == '__main__':
    test_detail_endpoint()
    list_all_endpoints() 