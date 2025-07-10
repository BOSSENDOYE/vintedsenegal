# 🔧 Guide de Dépannage - Erreur 401

## Problème
Erreur 401 (Unauthorized) lors de la connexion à l'application Vinted.

## Solutions

### 1. Installation des Dépendances Backend

```bash
cd backend
pip install -r requirements.txt
```

**Dépendances requises :**
- `djangorestframework-simplejwt>=5.2,<6.0`
- `django-cors-headers>=4.0,<5.0`
- `mysqlclient>=2.1,<3.0`

### 2. Configuration de la Base de Données

Assurez-vous que MySQL est configuré correctement dans `backend/project/settings.py` :

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'vinted',
        'USER': 'root',
        'PASSWORD': 'Oumou@245',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

### 3. Migration de la Base de Données

```bash
cd backend
python manage.py makemigrations
python manage.py migrate
```

### 4. Création d'un Super Utilisateur

```bash
cd backend
python manage.py createsuperuser
```

### 5. Test de l'Authentification

Exécutez le script de test pour diagnostiquer :

```bash
cd backend
python test_auth.py
```

### 6. Vérification du Serveur Backend

Assurez-vous que le serveur Django fonctionne :

```bash
cd backend
python manage.py runserver
```

Le serveur doit être accessible sur `http://localhost:8000`

### 7. Vérification du Frontend

Assurez-vous que le frontend pointe vers la bonne URL API :

Dans `frontend/src/services/api.js` :
```javascript
baseURL: process.env.REACT_APP_API_URL || 'http://localhost:8000/api'
```

### 8. Test Manuel de l'API

Testez l'API avec curl :

```bash
# Test de connexion
curl -X POST http://localhost:8000/api/users/login/ \
  -H "Content-Type: application/json" \
  -d '{"username": "testuser", "password": "testpass123"}'
```

### 9. Vérification des CORS

Assurez-vous que CORS est configuré dans `backend/project/settings.py` :

```python
CORS_ALLOW_ALL_ORIGINS = True
```

### 10. Redémarrage des Services

1. Arrêtez le serveur Django (Ctrl+C)
2. Arrêtez le serveur React (Ctrl+C)
3. Redémarrez le serveur Django :
   ```bash
   cd backend
   python manage.py runserver
   ```
4. Redémarrez le serveur React :
   ```bash
   cd frontend
   npm start
   ```

## Messages d'Erreur Courants

### "ModuleNotFoundError: No module named 'rest_framework_simplejwt'"
**Solution :** Installez les dépendances JWT
```bash
pip install djangorestframework-simplejwt
```

### "MySQL connection failed"
**Solution :** Vérifiez la configuration MySQL et installez mysqlclient
```bash
pip install mysqlclient
```

### "CORS error"
**Solution :** Vérifiez que django-cors-headers est installé et configuré
```bash
pip install django-cors-headers
```

## Test de Diagnostic

Le script `test_auth.py` va :
1. Créer un utilisateur de test
2. Tester la connexion API
3. Tester l'accès à un endpoint protégé

Si tous les tests passent, l'authentification fonctionne correctement.

## Contact

Si le problème persiste, vérifiez :
- Les logs du serveur Django
- La console du navigateur (F12)
- La configuration de la base de données
- Les variables d'environnement 