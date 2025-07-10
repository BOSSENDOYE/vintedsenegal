#!/bin/bash

echo "🚀 Démarrage de Vinted - Environnement de Développement"
echo "=================================================="

# Couleurs pour les messages
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Fonction pour afficher les messages
print_status() {
    echo -e "${GREEN}✅ $1${NC}"
}

print_warning() {
    echo -e "${YELLOW}⚠️  $1${NC}"
}

print_error() {
    echo -e "${RED}❌ $1${NC}"
}

# Vérifier si Python est installé
if ! command -v python3 &> /dev/null; then
    print_error "Python 3 n'est pas installé. Veuillez l'installer d'abord."
    exit 1
fi

# Vérifier si Node.js est installé
if ! command -v node &> /dev/null; then
    print_error "Node.js n'est pas installé. Veuillez l'installer d'abord."
    exit 1
fi

# Vérifier si MySQL est installé
if ! command -v mysql &> /dev/null; then
    print_warning "MySQL n'est pas installé ou n'est pas dans le PATH."
    print_warning "Assurez-vous que MySQL est installé et en cours d'exécution."
fi

print_status "Vérification des prérequis terminée"

# Backend Setup
echo ""
echo "🔧 Configuration du Backend..."
cd backend

# Vérifier si l'environnement virtuel existe
if [ ! -d "venv" ]; then
    print_status "Création de l'environnement virtuel Python..."
    python3 -m venv venv
fi

# Activer l'environnement virtuel
print_status "Activation de l'environnement virtuel..."
source venv/bin/activate

# Installer les dépendances
print_status "Installation des dépendances Python..."
pip install -r requirements.txt

# Vérifier si les migrations sont nécessaires
print_status "Vérification des migrations de base de données..."
python manage.py makemigrations --dry-run > /dev/null 2>&1
if [ $? -eq 0 ]; then
    print_status "Application des migrations..."
    python manage.py makemigrations
    python manage.py migrate
else
    print_warning "Erreur lors de la vérification des migrations. Vérifiez la configuration de la base de données."
fi

# Créer un super utilisateur si nécessaire
echo ""
print_status "Création d'un utilisateur de test..."
python manage.py shell -c "
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username='testuser').exists():
    user = User.objects.create_user(
        username='testuser',
        email='test@example.com',
        password='testpass123'
    )
    print('Utilisateur test créé: testuser / testpass123')
else:
    print('Utilisateur test existe déjà')
"

# Test de l'authentification
echo ""
print_status "Test de l'authentification..."
python test_auth.py

# Démarrer le serveur backend en arrière-plan
echo ""
print_status "Démarrage du serveur backend..."
python manage.py runserver 0.0.0.0:8000 &
BACKEND_PID=$!

# Attendre que le serveur backend démarre
sleep 3

# Frontend Setup
echo ""
echo "🎨 Configuration du Frontend..."
cd ../frontend

# Installer les dépendances Node.js
print_status "Installation des dépendances Node.js..."
npm install

# Démarrer le serveur frontend
echo ""
print_status "Démarrage du serveur frontend..."
npm start &
FRONTEND_PID=$!

# Attendre que le serveur frontend démarre
sleep 5

echo ""
echo "🎉 Environnement de développement démarré !"
echo "=========================================="
echo ""
echo "📱 Frontend: http://localhost:3000"
echo "🔧 Backend:  http://localhost:8000"
echo "📊 Admin:    http://localhost:8000/admin"
echo ""
echo "👤 Utilisateur de test:"
echo "   Username: testuser"
echo "   Password: testpass123"
echo ""
echo "🛑 Pour arrêter les serveurs, appuyez sur Ctrl+C"
echo ""

# Fonction de nettoyage
cleanup() {
    echo ""
    print_status "Arrêt des serveurs..."
    kill $BACKEND_PID 2>/dev/null
    kill $FRONTEND_PID 2>/dev/null
    print_status "Serveurs arrêtés. Au revoir !"
    exit 0
}

# Capturer Ctrl+C
trap cleanup SIGINT

# Attendre indéfiniment
wait 