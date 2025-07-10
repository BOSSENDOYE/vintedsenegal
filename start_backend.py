#!/usr/bin/env python3
"""
Script de démarrage rapide pour le backend
"""

import os
import sys
import subprocess
import time

def run_command(command, description):
    """Exécuter une commande avec description"""
    print(f"\n🔄 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} terminé")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Erreur lors de {description}:")
        print(f"   {e.stderr}")
        return False

def main():
    print("🚀 Démarrage du backend Vinted")
    print("=" * 50)
    
    # Vérifier que nous sommes dans le bon répertoire
    if not os.path.exists('backend/manage.py'):
        print("❌ Erreur: Ce script doit être exécuté depuis la racine du projet")
        return
    
    # Aller dans le répertoire backend
    os.chdir('backend')
    
    # 1. Vérifier les migrations
    if not run_command('python manage.py makemigrations', "Vérification des migrations"):
        return
    
    # 2. Appliquer les migrations
    if not run_command('python manage.py migrate', "Application des migrations"):
        return
    
    # 3. Créer les données de test
    if not run_command('python diagnostic.py', "Création des données de test"):
        return
    
    # 4. Démarrer le serveur
    print("\n🌐 Démarrage du serveur Django...")
    print("   Le serveur sera accessible sur: http://localhost:8000")
    print("   Appuyez sur Ctrl+C pour arrêter le serveur")
    print("=" * 50)
    
    try:
        subprocess.run('python manage.py runserver', shell=True)
    except KeyboardInterrupt:
        print("\n👋 Serveur arrêté")

if __name__ == '__main__':
    main() 