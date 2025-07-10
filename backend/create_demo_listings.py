#!/usr/bin/env python3
"""
Script pour créer des annonces de démonstration
"""

import os
import sys
import django
from django.conf import settings

# Configuration Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

from listings.models import Category, Listing
from django.contrib.auth import get_user_model

User = get_user_model()

def create_demo_listings():
    """Créer des annonces de démonstration"""
    print("🎨 Création d'annonces de démonstration")
    print("=" * 50)
    
    # Récupérer l'utilisateur de test
    try:
        user = User.objects.get(username='testuser')
        print(f"✅ Utilisateur trouvé: {user.username}")
    except User.DoesNotExist:
        print("❌ Utilisateur 'testuser' non trouvé")
        print("💡 Exécutez d'abord: python quick_test.py")
        return
    
    # Récupérer les catégories
    categories = Category.objects.all()
    if not categories.exists():
        print("❌ Aucune catégorie trouvée")
        print("💡 Exécutez d'abord: python create_categories.py")
        return
    
    print(f"✅ {categories.count()} catégories trouvées")
    
    # Données des annonces de démonstration
    demo_listings = [
        {
            'title': 'Robe traditionnelle sénégalaise en wax',
            'description': 'Magnifique robe traditionnelle en wax authentique, parfait état, taille M. Idéale pour les cérémonies et événements spéciaux.',
            'price': 25000,
            'category': 'Femmes'
        },
        {
            'title': 'Sneakers Nike Air Max 270',
            'description': 'Sneakers Nike Air Max 270 en excellent état, pointure 42. Très confortables pour le sport ou la ville.',
            'price': 35000,
            'category': 'Hommes'
        },
        {
            'title': 'Sac à main cuir véritable',
            'description': 'Sac à main en cuir véritable de qualité, marron, avec plusieurs compartiments. Parfait pour le travail.',
            'price': 45000,
            'category': 'Femmes'
        },
        {
            'title': 'Smartphone Samsung Galaxy A52',
            'description': 'Smartphone Samsung Galaxy A52, 128GB, bleu, en très bon état. Livré avec chargeur et coque de protection.',
            'price': 120000,
            'category': 'Électronique'
        },
        {
            'title': 'Livre "Le Petit Prince" en français',
            'description': 'Édition collector du Petit Prince d\'Antoine de Saint-Exupéry, en parfait état. Idéal pour collectionneurs.',
            'price': 5000,
            'category': 'Livres'
        },
        {
            'title': 'Ballon de football Adidas',
            'description': 'Ballon de football officiel Adidas, taille 5, utilisé seulement quelques fois. Parfait pour l\'entraînement.',
            'price': 15000,
            'category': 'Sport'
        },
        {
            'title': 'Vase décoratif en céramique',
            'description': 'Vase décoratif en céramique artisanale, motif traditionnel africain. Parfait pour décorer votre salon.',
            'price': 18000,
            'category': 'Maison'
        },
        {
            'title': 'Jeu de société Monopoly',
            'description': 'Jeu de société Monopoly complet, toutes les pièces présentes. Parfait pour les soirées en famille.',
            'price': 8000,
            'category': 'Loisirs'
        }
    ]
    
    created_count = 0
    for listing_data in demo_listings:
        try:
            # Trouver la catégorie
            category = Category.objects.get(name=listing_data['category'])
            
            # Créer l'annonce
            listing, created = Listing.objects.get_or_create(
                title=listing_data['title'],
                defaults={
                    'description': listing_data['description'],
                    'price': listing_data['price'],
                    'category': category,
                    'seller': user
                }
            )
            
            if created:
                print(f"✅ Annonce créée: {listing.title}")
                created_count += 1
            else:
                print(f"ℹ️ Annonce existante: {listing.title}")
                
        except Category.DoesNotExist:
            print(f"❌ Catégorie '{listing_data['category']}' non trouvée")
        except Exception as e:
            print(f"❌ Erreur lors de la création: {e}")
    
    # Statistiques finales
    print(f"\n📊 Résumé:")
    print(f"   - {created_count} nouvelles annonces créées")
    print(f"   - {Listing.objects.count()} annonces totales")
    
    # Lister toutes les annonces
    print(f"\n📋 Toutes les annonces:")
    for listing in Listing.objects.all().order_by('-created_at'):
        print(f"   - {listing.title} ({listing.category.name}) - {listing.price} FCFA")
    
    print(f"\n🎉 Annonces de démonstration créées avec succès!")
    print(f"💡 Vous pouvez maintenant voir ces annonces sur la page d'accueil")

if __name__ == '__main__':
    create_demo_listings() 