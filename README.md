# 🛍️ Vinted Dakar - Plateforme de Vente d'Occasion

Une plateforme moderne de vente d'articles d'occasion, spécialement conçue pour le marché sénégalais.

## 🚀 Démarrage Rapide

### Option 1: Script Automatique (Recommandé)

**Windows :**
```bash
start_dev.bat
```

**Linux/Mac :**
```bash
chmod +x start_dev.sh
./start_dev.sh
```

### Option 2: Installation Manuelle

#### Prérequis
- Python 3.8+
- Node.js 14+
- MySQL 8.0+

#### Backend Setup
```bash
cd backend

# Créer l'environnement virtuel
python -m venv venv

# Activer l'environnement virtuel
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Installer les dépendances
pip install -r requirements.txt

# Configurer la base de données
python manage.py makemigrations
python manage.py migrate

# Créer un utilisateur de test
python manage.py shell -c "
from django.contrib.auth import get_user_model
User = get_user_model()
user, created = User.objects.get_or_create(
    username='testuser',
    defaults={'email': 'test@example.com'}
)
user.set_password('testpass123')
user.save()
print('Utilisateur test créé: testuser / testpass123' if created else 'Utilisateur test existe déjà')
"

# Démarrer le serveur
python manage.py runserver
```

#### Frontend Setup
```bash
cd frontend

# Installer les dépendances
npm install

# Démarrer le serveur de développement
npm start
```

## 🔧 Résolution de l'Erreur 401

Si vous rencontrez une erreur 401 lors de la connexion, suivez ces étapes :

### 1. Vérifier les Dépendances Backend
```bash
cd backend
pip install djangorestframework-simplejwt
pip install django-cors-headers
pip install mysqlclient
```

### 2. Tester l'Authentification
```bash
cd backend
python test_auth.py
```

### 3. Vérifier la Configuration
- Assurez-vous que MySQL est en cours d'exécution
- Vérifiez les paramètres de base de données dans `backend/project/settings.py`
- Confirmez que CORS est configuré

### 4. Redémarrer les Services
1. Arrêtez les serveurs (Ctrl+C)
2. Redémarrez le backend : `python manage.py runserver`
3. Redémarrez le frontend : `npm start`

## 📱 Fonctionnalités

### Pour les Vendeurs
- ✅ **Dashboard complet** avec statistiques en temps réel
- ✅ **Gestion des annonces** (créer, modifier, supprimer)
- ✅ **Suivi des performances** (vues, messages, ventes)
- ✅ **Interface intuitive** avec navigation latérale
- ✅ **Notifications modernes** pour les actions importantes

### Pour les Acheteurs
- ✅ **Catalogue complet** avec filtres avancés
- ✅ **Recherche intelligente** par catégorie et mots-clés
- ✅ **Détails des annonces** avec photos et descriptions
- ✅ **Système de messagerie** pour contacter les vendeurs

## 🏗️ Architecture

### Backend (Django REST Framework)
- **Authentification JWT** sécurisée
- **API RESTful** complète
- **Base de données MySQL** performante
- **CORS configuré** pour le développement

### Frontend (React)
- **Interface moderne** avec Tailwind CSS
- **Gestion d'état** avec Context API
- **Navigation fluide** avec React Router
- **Composants réutilisables** et modulaires

## 🔐 Authentification

### Utilisateur de Test
- **Username:** `testuser`
- **Password:** `testpass123`
- **Email:** `test@example.com`

### Créer un Nouveau Compte
1. Allez sur `/register`
2. Remplissez le formulaire
3. Connectez-vous avec vos identifiants

## 📊 Dashboard Vendeur

Le dashboard offre :
- **Statistiques en temps réel** (annonces, vues, ventes)
- **Actions rapides** (créer annonce, gérer messages)
- **Vue d'ensemble** des performances
- **Conseils personnalisés** pour améliorer les ventes

## 🛠️ Développement

### Structure du Projet
```
vinteddd/
├── backend/                 # API Django
│   ├── users/              # Authentification
│   ├── listings/           # Gestion des annonces
│   ├── messaging/          # Système de messages
│   └── project/            # Configuration Django
├── frontend/               # Application React
│   ├── src/
│   │   ├── components/     # Composants réutilisables
│   │   ├── pages/          # Pages de l'application
│   │   ├── services/       # Services API
│   │   └── context/        # Gestion d'état
│   └── public/             # Fichiers statiques
└── docs/                   # Documentation
```

### Scripts Utiles
- `test_auth.py` - Test de l'authentification
- `start_dev.bat` - Démarrage automatique (Windows)
- `start_dev.sh` - Démarrage automatique (Linux/Mac)

## 🐛 Dépannage

### Erreurs Courantes

**Erreur 401 - Non autorisé**
- Vérifiez que les dépendances JWT sont installées
- Testez avec le script `test_auth.py`
- Redémarrez les serveurs

**Erreur de base de données**
- Vérifiez que MySQL est en cours d'exécution
- Appliquez les migrations : `python manage.py migrate`

**Erreur CORS**
- Vérifiez que `django-cors-headers` est installé
- Confirmez la configuration CORS dans `settings.py`

### Logs et Debug
- **Backend:** Vérifiez la console Django
- **Frontend:** Ouvrez les outils de développement (F12)
- **Base de données:** Vérifiez les logs MySQL

## 📞 Support

Pour toute question ou problème :
1. Consultez le fichier `TROUBLESHOOTING.md`
2. Exécutez le script de test : `python test_auth.py`
3. Vérifiez les logs des serveurs

## 🚀 Déploiement

### Production
1. Configurez les variables d'environnement
2. Utilisez un serveur WSGI (Gunicorn)
3. Configurez un serveur web (Nginx)
4. Utilisez une base de données de production

### Variables d'Environnement
```bash
# Backend
SECRET_KEY=your-secret-key
DEBUG=False
DATABASE_URL=mysql://user:pass@host:port/db

# Frontend
REACT_APP_API_URL=https://your-api-domain.com/api
```

---

**Développé avec ❤️ pour le marché sénégalais** 