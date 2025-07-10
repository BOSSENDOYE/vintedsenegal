#!/usr/bin/env python3
"""
Script de configuration complète pour les annonces
"""

import os
import sys
import django
from django.conf import settings

# Configuration Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

from listings.models import Category, Listing, Photo
from django.contrib.auth import get_user_model

User = get_user_model()

def setup_listings():
    """Configuration complète des annonces"""
    print("🚀 Configuration des annonces")
    print("=" * 50)
    
    # 1. Créer les catégories
    print("\n1️⃣ Création des catégories...")
    categories_data = [
        "Femmes",
        "Hommes", 
        "Enfants",
        "Maison",
        "Loisirs",
        "Livres",
        "Sport",
        "Électronique",
        "Automobile",
        "Autres"
    ]
    
    for cat_name in categories_data:
        category, created = Category.objects.get_or_create(name=cat_name)
        if created:
            print(f"   ✅ {cat_name}")
        else:
            print(f"   ℹ️ {cat_name} (existant)")
    
    # 2. Vérifier qu'il y a un utilisateur de test
    print("\n2️⃣ Vérification de l'utilisateur de test...")
    try:
        test_user = User.objects.get(username='testuser')
        print(f"   ✅ Utilisateur trouvé: {test_user.username}")
    except User.DoesNotExist:
        print("   ❌ Utilisateur 'testuser' non trouvé")
        print("   💡 Exécutez d'abord: python quick_test.py")
        return
    
    # 3. Créer une annonce de test
    print("\n3️⃣ Création d'une annonce de test...")
    try:
        category = Category.objects.get(name='Femmes')
        listing, created = Listing.objects.get_or_create(
            title='Robe traditionnelle sénégalaise',
            defaults={
                'description': 'Belle robe traditionnelle en wax, parfait état',
                'category': category,
                'price': 15000,
                'seller': test_user
            }
        )
        if created:
            print(f"   ✅ Annonce créée: {listing.title}")
        else:
            print(f"   ℹ️ Annonce existante: {listing.title}")
    except Exception as e:
        print(f"   ❌ Erreur: {e}")
    
    # 4. Statistiques
    print("\n4️⃣ Statistiques:")
    print(f"   📊 Catégories: {Category.objects.count()}")
    print(f"   📊 Annonces: {Listing.objects.count()}")
    print(f"   📊 Photos: {Photo.objects.count()}")
    
    print("\n🎉 Configuration terminée!")
    print("\n💡 Prochaines étapes:")
    print("   1. Redémarrer le serveur Django")
    print("   2. Tester la création d'annonce depuis le frontend")

if __name__ == '__main__':
    setup_listings() 