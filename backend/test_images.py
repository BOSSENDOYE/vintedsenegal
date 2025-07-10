#!/usr/bin/env python3
"""
Script pour tester les images et créer des annonces avec des images de démonstration
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
from django.core.files.base import ContentFile
import requests
from io import BytesIO

User = get_user_model()

def download_image(url, filename):
    """Télécharger une image depuis une URL"""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return ContentFile(response.content, name=filename)
    except Exception as e:
        print(f"❌ Erreur lors du téléchargement de {url}: {e}")
        return None

def create_listings_with_images():
    """Créer des annonces avec des images de démonstration"""
    print("🖼️ Création d'annonces avec images")
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
    
    # Données des annonces avec images
    demo_listings = [
        {
            'title': 'Robe traditionnelle sénégalaise en wax',
            'description': 'Magnifique robe traditionnelle en wax authentique, parfait état, taille M. Idéale pour les cérémonies et événements spéciaux. Couleurs vives et motifs traditionnels.',
            'price': 25000,
            'category': 'Femmes',
            'images': [
                'https://images.unsplash.com/photo-1594633312681-425c7b97ccd1?w=400&h=300&fit=crop',
                'https://images.unsplash.com/photo-1594633312681-425c7b97ccd1?w=400&h=300&fit=crop'
            ]
        },
        {
            'title': 'Sneakers Nike Air Max 270',
            'description': 'Sneakers Nike Air Max 270 en excellent état, pointure 42. Très confortables pour le sport ou la ville. Couleur blanche avec détails noirs.',
            'price': 35000,
            'category': 'Hommes',
            'images': [
                'https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=400&h=300&fit=crop'
            ]
        },
        {
            'title': 'Sac à main cuir véritable',
            'description': 'Sac à main en cuir véritable de qualité, marron, avec plusieurs compartiments. Parfait pour le travail. Marque de luxe, très peu utilisée.',
            'price': 45000,
            'category': 'Femmes',
            'images': [
                'https://images.unsplash.com/photo-1584917865442-de89df76afd3?w=400&h=300&fit=crop'
            ]
        },
        {
            'title': 'Smartphone Samsung Galaxy A52',
            'description': 'Smartphone Samsung Galaxy A52, 128GB, bleu, en très bon état. Livré avec chargeur et coque de protection. Écran parfait, batterie en bon état.',
            'price': 120000,
            'category': 'Électronique',
            'images': [
                'https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?w=400&h=300&fit=crop'
            ]
        },
        {
            'title': 'Livre "Le Petit Prince" en français',
            'description': 'Édition collector du Petit Prince d\'Antoine de Saint-Exupéry, en parfait état. Idéal pour collectionneurs. Reliure en cuir, illustrations originales.',
            'price': 5000,
            'category': 'Livres',
            'images': [
                'https://images.unsplash.com/photo-1544947950-fa07a98d237f?w=400&h=300&fit=crop'
            ]
        },
        {
            'title': 'Ballon de football Adidas',
            'description': 'Ballon de football officiel Adidas, taille 5, utilisé seulement quelques fois. Parfait pour l\'entraînement. Couleur blanche et noir.',
            'price': 15000,
            'category': 'Sport',
            'images': [
                'https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b?w=400&h=300&fit=crop'
            ]
        },
        {
            'title': 'Vase décoratif en céramique',
            'description': 'Vase décoratif en céramique artisanale, motif traditionnel africain. Parfait pour décorer votre salon. Hauteur 30cm, couleur terre cuite.',
            'price': 18000,
            'category': 'Maison',
            'images': [
                'https://images.unsplash.com/photo-1578662996442-48f60103fc96?w=400&h=300&fit=crop'
            ]
        },
        {
            'title': 'Jeu de société Monopoly',
            'description': 'Jeu de société Monopoly complet, toutes les pièces présentes. Parfait pour les soirées en famille. Version française, boîte en bon état.',
            'price': 8000,
            'category': 'Loisirs',
            'images': [
                'https://images.unsplash.com/photo-1610890716171-6b1bb98ffd09?w=400&h=300&fit=crop'
            ]
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
            
            # Ajouter les images
            for i, image_url in enumerate(listing_data['images']):
                image_file = download_image(image_url, f"{listing.title}_{i}.jpg")
                if image_file:
                    photo = Photo.objects.create(
                        listing=listing,
                        image=image_file
                    )
                    print(f"   📸 Image {i+1} ajoutée")
                else:
                    print(f"   ❌ Échec de l'ajout de l'image {i+1}")
                
        except Category.DoesNotExist:
            print(f"❌ Catégorie '{listing_data['category']}' non trouvée")
        except Exception as e:
            print(f"❌ Erreur lors de la création: {e}")
    
    # Statistiques finales
    print(f"\n📊 Résumé:")
    print(f"   - {created_count} nouvelles annonces créées")
    print(f"   - {Listing.objects.count()} annonces totales")
    print(f"   - {Photo.objects.count()} photos totales")
    
    # Lister toutes les annonces avec leurs photos
    print(f"\n📋 Toutes les annonces:")
    for listing in Listing.objects.all().order_by('-created_at'):
        photo_count = listing.photos.count()
        print(f"   - {listing.title} ({listing.category.name}) - {listing.price} FCFA - {photo_count} photo(s)")
    
    print(f"\n🎉 Annonces avec images créées avec succès!")
    print(f"💡 Vous pouvez maintenant voir ces annonces avec leurs images sur la page d'accueil")

if __name__ == '__main__':
    create_listings_with_images() 