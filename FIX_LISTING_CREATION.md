# 🔧 Résolution - Erreur 500 Création d'Annonce

## Problème
Erreur 500 lors de la création d'une annonce avec le message "Request failed with status code 500".

## Solutions

### 1. Configuration de la Base de Données

#### A. Créer les Migrations
```bash
cd backend
python manage.py makemigrations listings
python manage.py migrate
```

#### B. Créer les Catégories
```bash
python create_categories.py
```

#### C. Configuration Complète
```bash
python setup_listings.py
```

### 2. Vérifier l'Utilisateur de Test

#### A. Créer un Utilisateur
```bash
python quick_test.py
```

#### B. Vérifier la Connexion
```bash
python create_test_user.py
```

### 3. Tester l'API Manuellement

#### A. Test avec curl
```bash
# D'abord se connecter
curl -X POST http://localhost:8000/api/users/login/ \
  -H "Content-Type: application/json" \
  -d '{"username": "testuser", "password": "testpass123"}'

# Puis créer une annonce (remplacer TOKEN par le token reçu)
curl -X POST http://localhost:8000/api/listings/create/ \
  -H "Authorization: Bearer TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Test Annonce",
    "description": "Description test",
    "price": "10000",
    "category": "Femmes"
  }'
```

### 4. Vérifier les Logs Django

#### A. Activer les Logs Détaillés
Dans `backend/project/settings.py`, ajouter :
```python
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'INFO',
    },
}
```

#### B. Redémarrer le Serveur
```bash
python manage.py runserver
```

### 5. Vérifier les Permissions

#### A. Vérifier l'Authentification
- L'utilisateur doit être connecté
- Le token JWT doit être valide
- L'en-tête Authorization doit être présent

#### B. Vérifier les Données
- Tous les champs obligatoires doivent être remplis
- Le prix doit être un nombre valide
- La catégorie doit exister dans la base de données

### 6. Test Complet

#### A. Script de Test
```bash
python test_listing_creation.py
```

#### B. Vérifier les Résultats
- Status 201: Succès
- Status 400: Données invalides
- Status 401: Non authentifié
- Status 500: Erreur serveur

## Structure Attendue

### Données d'Entrée
```json
{
  "title": "Titre de l'annonce",
  "description": "Description détaillée",
  "price": "15000",
  "category": "Femmes",
  "images": [File1, File2, ...]
}
```

### Réponse de Succès
```json
{
  "id": 1,
  "title": "Titre de l'annonce",
  "description": "Description détaillée",
  "category": "Femmes",
  "price": "15000.00",
  "seller": "testuser",
  "created_at": "2024-01-01T12:00:00Z",
  "photos": []
}
```

## Erreurs Courantes

### 1. "Category matching query does not exist"
- **Solution**: Exécuter `python create_categories.py`

### 2. "User matching query does not exist"
- **Solution**: Exécuter `python quick_test.py`

### 3. "Permission denied"
- **Solution**: Vérifier l'authentification et le token JWT

### 4. "Invalid data"
- **Solution**: Vérifier que tous les champs obligatoires sont remplis

## Contact
Si le problème persiste, vérifiez :
- Les logs du serveur Django
- La console du navigateur (F12)
- La configuration de la base de données
- Les permissions des fichiers d'upload 