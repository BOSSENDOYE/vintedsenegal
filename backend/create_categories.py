#!/usr/bin/env python3
"""
Script pour créer les catégories dans la base de données
"""

import os
import sys
import django
from django.conf import settings

# Configuration Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

from listings.models import Category

def create_categories():
    """Créer les catégories principales"""
    print("🏷️ Création des catégories")
    print("=" * 50)
    
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
    
    created_count = 0
    for cat_name in categories_data:
        category, created = Category.objects.get_or_create(name=cat_name)
        if created:
            print(f"✅ Catégorie créée: {cat_name}")
            created_count += 1
        else:
            print(f"ℹ️ Catégorie existante: {cat_name}")
    
    print(f"\n📊 Résumé: {created_count} nouvelles catégories créées")
    
    # Lister toutes les catégories
    print("\n📋 Toutes les catégories:")
    for cat in Category.objects.all():
        print(f"   - {cat.name} (ID: {cat.id})")

if __name__ == '__main__':
    create_categories() 