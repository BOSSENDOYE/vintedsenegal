#!/usr/bin/env python3
"""
Test de l'inscription d'utilisateurs
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

def test_registration():
    """Tester l'inscription d'utilisateurs"""
    print("🧪 Test de l'inscription d'utilisateurs")
    print("=" * 50)
    
    client = Client()
    
    # Test 1: Inscription avec des données valides
    print("\n1️⃣ Test d'inscription avec données valides...")
    registration_data = {
        'username': 'newuser',
        'email': 'newuser@example.com',
        'first_name': 'Nouveau',
        'last_name': 'Utilisateur',
        'password': 'testpass123',
        'password2': 'testpass123'
    }
    
    response = client.post('/api/users/register/', 
                          data=json.dumps(registration_data),
                          content_type='application/json')
    
    print(f"Status: {response.status_code}")
    print(f"Response: {response.content.decode()}")
    
    if response.status_code == 201:
        print("✅ Inscription réussie!")
        
        # Vérifier que l'utilisateur existe
        try:
            user = User.objects.get(username='newuser')
            print(f"✅ Utilisateur créé: {user.username} (ID: {user.id})")
        except User.DoesNotExist:
            print("❌ Utilisateur non trouvé dans la base de données")
    else:
        print("❌ Échec de l'inscription")
    
    # Test 2: Inscription avec mot de passe différent
    print("\n2️⃣ Test avec mots de passe différents...")
    registration_data['username'] = 'testuser2'
    registration_data['email'] = 'testuser2@example.com'
    registration_data['password2'] = 'differentpass'
    
    response = client.post('/api/users/register/', 
                          data=json.dumps(registration_data),
                          content_type='application/json')
    
    print(f"Status: {response.status_code}")
    if response.status_code == 400:
        print("✅ Validation des mots de passe fonctionne")
    else:
        print("❌ Validation des mots de passe ne fonctionne pas")
    
    # Test 3: Inscription avec username existant
    print("\n3️⃣ Test avec username existant...")
    registration_data['username'] = 'testuser'  # Utilisateur existant
    registration_data['email'] = 'testuser3@example.com'
    registration_data['password2'] = 'testpass123'
    
    response = client.post('/api/users/register/', 
                          data=json.dumps(registration_data),
                          content_type='application/json')
    
    print(f"Status: {response.status_code}")
    if response.status_code == 400:
        print("✅ Validation username unique fonctionne")
    else:
        print("❌ Validation username unique ne fonctionne pas")
    
    # Test 4: Inscription avec email existant
    print("\n4️⃣ Test avec email existant...")
    registration_data['username'] = 'testuser4'
    registration_data['email'] = 'test@example.com'  # Email existant
    
    response = client.post('/api/users/register/', 
                          data=json.dumps(registration_data),
                          content_type='application/json')
    
    print(f"Status: {response.status_code}")
    if response.status_code == 400:
        print("✅ Validation email unique fonctionne")
    else:
        print("❌ Validation email unique ne fonctionne pas")

def test_login_after_registration():
    """Tester la connexion après inscription"""
    print("\n5️⃣ Test de connexion après inscription...")
    
    client = Client()
    
    # Créer un nouvel utilisateur
    registration_data = {
        'username': 'loginuser',
        'email': 'loginuser@example.com',
        'first_name': 'Login',
        'last_name': 'User',
        'password': 'testpass123',
        'password2': 'testpass123'
    }
    
    # Inscription
    response = client.post('/api/users/register/', 
                          data=json.dumps(registration_data),
                          content_type='application/json')
    
    if response.status_code == 201:
        print("✅ Utilisateur créé pour le test de connexion")
        
        # Connexion
        login_data = {
            'username': 'loginuser',
            'password': 'testpass123'
        }
        
        response = client.post('/api/users/login/', 
                              data=json.dumps(login_data),
                              content_type='application/json')
        
        print(f"Status de connexion: {response.status_code}")
        if response.status_code == 200:
            data = json.loads(response.content)
            print("✅ Connexion réussie après inscription!")
            print(f"   Access Token: {data.get('access', 'Non trouvé')[:50]}...")
        else:
            print("❌ Échec de la connexion après inscription")
    else:
        print("❌ Impossible de créer l'utilisateur pour le test")

def list_users():
    """Lister tous les utilisateurs"""
    print("\n📋 Liste des utilisateurs:")
    print("=" * 30)
    
    users = User.objects.all()
    for user in users:
        print(f"   - {user.username} ({user.email}) - ID: {user.id}")

if __name__ == '__main__':
    test_registration()
    test_login_after_registration()
    list_users()
    
    print("\n🎯 Résumé:")
    print("=" * 30)
    print("1. Vérifiez que l'inscription fonctionne")
    print("2. Vérifiez que la connexion après inscription fonctionne")
    print("3. Vérifiez que les validations fonctionnent")
    print("4. Vérifiez que les utilisateurs sont créés dans la base de données") 